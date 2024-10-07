import ply.lex as lex
import ply.yacc as yacc
from flask import Flask, render_template, request

app = Flask(__name__)

# Lista de tokens
tokens = ['PROGRAMA', 'INT', 'READ', 'PRINTF', 'END', 'SUMA', 'LPAREN', 
          'RPAREN', 'LBRACE', 'RBRACE', 'COMA', 'SEMICOLON', 'ADICION', 
          'IGUAL', 'IDENTIFICADOR', 'VARIABLE', 'CADENA']

reservada = {
    "programa": "PROGRAMA",
    "int": "INT",
    "read": "READ",
    "printf": "PRINTF",
    "end": "END"
}

simbolo = {
    "(": "LPAREN",
    ")": "RPAREN",
    "{": "LBRACE", 
    "}": "RBRACE",
    ",": "COMA",
    ";": "SEMICOLON",
    "+": "ADICION",
    "=": "IGUAL"
}

# Reglas de expresión regular para los tokens simples
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMA = r'\,'
t_SEMICOLON = r';'
t_ADICION = r'\+'
t_IGUAL = r'='

# Definición de palabras clave y variables
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservada.get(t.value, 'IDENTIFICADOR')
    return t

def t_CADENA(t):
    r'"[^"]*"'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Definición del parser (sintaxis)
errors = []
variables_declaradas = set()

def p_funcion(p):
    '''funcion : PROGRAMA IDENTIFICADOR LPAREN RPAREN LBRACE estructura RBRACE'''
    if not errors:
        print("Ningún error sintáctico!")

def p_estructura(p):
    'estructura : variables entrada operacion impresion salida'
    pass

def p_variables(p):
    '''variables : INT IDENTIFICADOR COMA IDENTIFICADOR COMA IDENTIFICADOR SEMICOLON'''
    global variables_declaradas
    variables_declaradas.update([p[2], p[4], p[6]])
    print("Variables correctamente declaradas ", variables_declaradas)

def p_entrada(p):
    '''entrada : lectura lectura'''

def p_lectura(p):
    '''lectura : READ IDENTIFICADOR SEMICOLON'''
    if p[2] not in variables_declaradas:
        errors.append(f"Error: Variable '{p[2]}' no declarada en la línea {p.lineno(2)}")

def p_operacion(p):
    '''operacion : IDENTIFICADOR IGUAL IDENTIFICADOR ADICION IDENTIFICADOR SEMICOLON'''
    if p[1] not in variables_declaradas:
        errors.append(f"Error: Variable '{p[1]}' no declarada en la línea {p.lineno(1)}")
    if p[3] not in variables_declaradas:
        errors.append(f"Error: Variable '{p[3]}' no declarada en la línea {p.lineno(3)}")
    if p[5] not in variables_declaradas:
        errors.append(f"Error: Variable '{p[5]}' no declarada en la línea {p.lineno(5)}")

def p_impresion(p):
    '''impresion : PRINTF LPAREN CADENA RPAREN'''

def p_salida(p):
    '''salida : END SEMICOLON'''

def p_error(p):
    if p:
        errors.append(f"Error de sintaxis en la línea {p.lineno}")
    else:
        errors.append("Error de sintaxis al final del archivo")

parser = yacc.yacc()

# Función para analizar el código
def analyze_code(code):
    global variables_declaradas, errors
    variables_declaradas = set()  # Reiniciar variables declaradas
    errors = []  # Reiniciar lista de errores
    tokens_list = []
    sintactic_list = []
    lexer.lineno = 1  # Reiniciar el contador de líneas
    lexer.input(code)

    # Diccionario para contar tokens por tipo
    token_count = {
        'PROGRAMA': 0,
        'INT': 0,
        'READ': 0,
        'PRINTF': 0,
        'END': 0,
        'IDENTIFICADOR': 0,
        'CADENA': 0,
        'SÍMBOLOS': 0  # Para símbolos como +, =, etc.
    }

    # Recopilar todos los tokens léxicos
    for token in lexer:
        tokens_list.append({"token": token.type, "lexema": str(token.value), "linea": token.lineno})

        # Identificar el tipo de token para el análisis sintáctico
        token_type = {
            'PR': 'X' if token.type in ['PROGRAMA', 'INT', 'READ', 'PRINTF', 'END'] else '',
            'ID': 'X' if token.type == 'IDENTIFICADOR' else '',
            'SÍM': 'X' if token.type in ['IGUAL', 'ADICION', 'SEMICOLON', 'COMA', 'RBRACE', 'LBRACE', 'RPAREN', 'LPAREN'] else '',
            'CAD': 'X' if token.type == 'CADENA' else '',
            'TIPO': ''  
        }

        # Contar tokens por tipo
        if token.type in ['PROGRAMA', 'INT', 'READ', 'PRINTF', 'END']:
            token_count[token.type] += 1
        elif token.type == 'IDENTIFICADOR':
            token_count['IDENTIFICADOR'] += 1
        elif token.type == 'CADENA':
            token_count['CADENA'] += 1
        else:
            token_count['SÍMBOLOS'] += 1

        sintactic_list.append({
            "token": token.type,
            "lexema": str(token.value),
            **token_type
        })

    syntax_error = None
    try:
        parser.parse(code, lexer=lexer)
    except SyntaxError as e:
        syntax_error = str(e)

    if errors:
        syntax_error = "\n".join(errors)

    return tokens_list, sintactic_list, token_count, syntax_error

# Rutas del servidor Flask
@app.route('/', methods=['GET', 'POST'])
def index():
    tokens = []
    sintactic_tokens = []
    token_count = None
    error = None

    if request.method == 'POST':
        code = request.form['code']
        tokens, sintactic_tokens, token_count, error = analyze_code(code)

    return render_template('index.html', tokens=tokens, sintactic_tokens=sintactic_tokens, token_count=token_count, error=error)

if __name__ == '__main__':
    app.run(debug=True)
