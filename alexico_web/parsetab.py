
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DOT EQUALS FOR IDENTIFIER INT LBRACE LESS_EQUAL LPAREN MENOS NUMBER OUT PLUS PLUS_PLUS PRINTLN RBRACE RPAREN SEMICOLON STRING SYSTEMprogram : for_loopfor_loop : FOR LPAREN INT IDENTIFIER EQUALS NUMBER SEMICOLON IDENTIFIER LESS_EQUAL NUMBER SEMICOLON increment RPAREN LBRACE statement RBRACEincrement : IDENTIFIER PLUS_PLUS\n                 | IDENTIFIER PLUS EQUALS NUMBERstatement : SYSTEM DOT OUT DOT PRINTLN LPAREN STRING PLUS IDENTIFIER RPAREN SEMICOLON'
    
_lr_action_items = {'FOR':([0,],[3,]),'$end':([1,2,24,],[0,-1,-2,]),'LPAREN':([3,28,],[4,29,]),'INT':([4,],[5,]),'IDENTIFIER':([5,9,13,31,],[6,10,14,32,]),'EQUALS':([6,17,],[7,19,]),'NUMBER':([7,11,19,],[8,12,21,]),'SEMICOLON':([8,12,33,],[9,13,34,]),'LESS_EQUAL':([10,],[11,]),'PLUS_PLUS':([14,],[16,]),'PLUS':([14,30,],[17,31,]),'RPAREN':([15,16,21,32,],[18,-3,-4,33,]),'LBRACE':([18,],[20,]),'SYSTEM':([20,],[23,]),'RBRACE':([22,34,],[24,-5,]),'DOT':([23,26,],[25,27,]),'OUT':([25,],[26,]),'PRINTLN':([27,],[28,]),'STRING':([29,],[30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'for_loop':([0,],[2,]),'increment':([13,],[15,]),'statement':([20,],[22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> for_loop','program',1,'p_program','app.py',79),
  ('for_loop -> FOR LPAREN INT IDENTIFIER EQUALS NUMBER SEMICOLON IDENTIFIER LESS_EQUAL NUMBER SEMICOLON increment RPAREN LBRACE statement RBRACE','for_loop',16,'p_for_loop','app.py',83),
  ('increment -> IDENTIFIER PLUS_PLUS','increment',2,'p_increment','app.py',87),
  ('increment -> IDENTIFIER PLUS EQUALS NUMBER','increment',4,'p_increment','app.py',88),
  ('statement -> SYSTEM DOT OUT DOT PRINTLN LPAREN STRING PLUS IDENTIFIER RPAREN SEMICOLON','statement',11,'p_statement','app.py',93),
]