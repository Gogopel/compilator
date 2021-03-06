
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BREAK CLOSE_FIG CLOSE_PAREN COMA CONTINUE DEF DIV DO DOUBLE_POINT ID IF INT LESS MORE MUL NOT NUMBER_INT NUMBER_REAL OPEN_FIG OPEN_PAREN OR PRINT PRISV RAVNO REAL RETURN SEMI_COLON STRING SUB SUM THEN VAR WHILEprog : VAR dec_list OPEN_FIG stmt_list CLOSE_FIG\n            | VAR dec_list def_list OPEN_FIG stmt_list CLOSE_FIGdef_list : def\n               | def_list SEMI_COLON defdef : DEF ID OPEN_PAREN dec_list CLOSE_PAREN OPEN_FIG stmt_list_def CLOSE_FIG\n            | DEF ID OPEN_PAREN dec_list CLOSE_PAREN OPEN_FIG VAR dec_list stmt_list_def CLOSE_FIGdefstmt : ID OPEN_PAREN args CLOSE_PARENargs : arg\n            | args SEMI_COLON argarg : ID\n            | NUMBER_INT\n            | NUMBER_REAL\n            | OPEN_PAREN exp CLOSE_PARENdec_list : dec\n               | dec_list SEMI_COLON decdec : id_list DOUBLE_POINT typetype : INT\n            | REAL\n            | STRINGid_list : ID\n                | id_list COMA IDstmt_list : stmt\n                | stmt_list SEMI_COLON stmtstmt : assign\n            | print\n            | while\n            | ifstmt_list_if : stmt_if\n                | stmt_list_if SEMI_COLON stmt_ifstmt_if : assign\n            | print\n            | while\n            | if\n            | CONTINUE\n            | BREAKstmt_list_def : stmt_def\n                | stmt_list_def SEMI_COLON stmt_defstmt_def : assign\n            | print\n            | while\n            | if\n            | returnreturn : RETURN expassign : ID PRISV exp\n                | ID PRISV STRINGexp : term\n            | exp SUM term\n            | exp SUB termterm : factor\n            | term MUL factor\n            | term DIV factorfactor : defstmt\n            | ID\n            | NUMBER_INT\n            | NUMBER_REAL\n            | OPEN_PAREN exp CLOSE_PARENprint : PRINT OPEN_PAREN exp CLOSE_PAREN\n                | PRINT OPEN_PAREN STRING CLOSE_PARENwhile : WHILE bool_exp DO OPEN_FIG stmt_list CLOSE_FIGif : IF bool_exp THEN OPEN_FIG stmt_list_if CLOSE_FIGbool_exp : bool_exp OR bool_exp_term\n                | bool_exp_term\n                | NOT bool_exp\n                | boolbool_exp_term : bool_exp_term AND bool\n                | boolbool : OPEN_PAREN exp RAVNO exp CLOSE_PAREN\n            | OPEN_PAREN exp MORE exp CLOSE_PAREN\n            | OPEN_PAREN exp LESS exp CLOSE_PAREN'
    
_lr_action_items = {'VAR':([0,106,],[2,117,]),'$end':([1,33,64,],[0,-1,-2,]),'ID':([2,4,7,9,11,13,24,26,28,29,30,31,34,35,36,41,45,55,66,67,68,69,70,74,78,79,80,81,84,106,109,115,117,124,129,130,],[6,-14,20,6,27,32,20,-15,-16,-17,-18,-19,20,47,47,47,6,47,83,47,47,47,47,20,47,47,47,20,47,20,83,20,6,47,20,20,]),'OPEN_FIG':([3,4,8,10,26,28,29,30,31,44,58,63,82,128,134,],[7,-14,24,-3,-15,-16,-17,-18,-19,-4,74,81,106,-5,-6,]),'SEMI_COLON':([3,4,8,10,14,15,16,17,18,19,26,28,29,30,31,43,44,46,47,48,49,50,51,52,53,54,65,72,73,83,85,86,87,88,89,90,91,92,93,94,98,99,100,101,102,103,104,105,108,110,114,116,118,119,120,121,122,123,125,126,127,128,130,131,132,133,134,],[9,-14,25,-3,34,-22,-24,-25,-26,-27,-15,-16,-17,-18,-19,34,-4,-23,-53,-44,-45,-46,-49,-52,-54,-55,9,-57,-58,-10,109,-8,-11,-12,-47,-48,-50,-51,-56,34,115,-28,-30,-31,-32,-33,-34,-35,-7,-59,-60,129,-36,-38,-39,-40,-41,-42,-13,-9,-29,-5,9,-43,-37,129,-6,]),'DEF':([3,4,25,26,28,29,30,31,],[11,-14,11,-15,-16,-17,-18,-19,]),'CLOSE_PAREN':([4,26,28,29,30,31,47,50,51,52,53,54,56,57,65,71,83,85,86,87,88,89,90,91,92,93,95,96,97,107,108,125,126,],[-14,-15,-16,-17,-18,-19,-53,-46,-49,-52,-54,-55,72,73,82,93,-10,108,-8,-11,-12,-47,-48,-50,-51,-56,111,112,113,125,-7,-13,-9,]),'PRINT':([4,7,24,26,28,29,30,31,34,74,81,106,115,129,130,],[-14,21,21,-15,-16,-17,-18,-19,21,21,21,21,21,21,21,]),'WHILE':([4,7,24,26,28,29,30,31,34,74,81,106,115,129,130,],[-14,22,22,-15,-16,-17,-18,-19,22,22,22,22,22,22,22,]),'IF':([4,7,24,26,28,29,30,31,34,74,81,106,115,129,130,],[-14,23,23,-15,-16,-17,-18,-19,23,23,23,23,23,23,23,]),'RETURN':([4,26,28,29,30,31,106,129,130,],[-14,-15,-16,-17,-18,-19,124,124,124,]),'DOUBLE_POINT':([5,6,32,],[12,-20,-21,]),'COMA':([5,6,32,],[13,-20,-21,]),'INT':([12,],[29,]),'REAL':([12,],[30,]),'STRING':([12,35,36,],[31,49,57,]),'CLOSE_FIG':([14,15,16,17,18,19,43,46,47,48,49,50,51,52,53,54,72,73,89,90,91,92,93,94,98,99,100,101,102,103,104,105,108,110,114,116,118,119,120,121,122,123,127,131,132,133,],[33,-22,-24,-25,-26,-27,64,-23,-53,-44,-45,-46,-49,-52,-54,-55,-57,-58,-47,-48,-50,-51,-56,110,114,-28,-30,-31,-32,-33,-34,-35,-7,-59,-60,128,-36,-38,-39,-40,-41,-42,-29,-43,-37,134,]),'PRISV':([20,],[35,]),'OPEN_PAREN':([21,22,23,27,35,36,39,41,47,55,59,60,66,67,68,69,70,78,79,80,84,109,124,],[36,41,41,45,55,55,41,55,66,55,41,41,84,55,55,55,55,55,55,55,55,84,55,]),'NOT':([22,23,39,],[39,39,39,]),'NUMBER_INT':([35,36,41,55,66,67,68,69,70,78,79,80,84,109,124,],[53,53,53,53,87,53,53,53,53,53,53,53,53,87,53,]),'NUMBER_REAL':([35,36,41,55,66,67,68,69,70,78,79,80,84,109,124,],[54,54,54,54,88,54,54,54,54,54,54,54,54,88,54,]),'DO':([37,38,40,61,75,76,77,111,112,113,],[58,-62,-64,-63,-61,-66,-65,-67,-68,-69,]),'OR':([37,38,40,42,61,75,76,77,111,112,113,],[59,-62,-64,59,59,-61,-66,-65,-67,-68,-69,]),'THEN':([38,40,42,61,75,76,77,111,112,113,],[-62,-64,63,-63,-61,-66,-65,-67,-68,-69,]),'AND':([38,40,75,76,77,111,112,113,],[60,-66,60,-66,-65,-67,-68,-69,]),'MUL':([47,50,51,52,53,54,89,90,91,92,93,108,],[-53,69,-49,-52,-54,-55,69,69,-50,-51,-56,-7,]),'DIV':([47,50,51,52,53,54,89,90,91,92,93,108,],[-53,70,-49,-52,-54,-55,70,70,-50,-51,-56,-7,]),'SUM':([47,48,50,51,52,53,54,56,62,71,89,90,91,92,93,95,96,97,107,108,131,],[-53,67,-46,-49,-52,-54,-55,67,67,67,-47,-48,-50,-51,-56,67,67,67,67,-7,67,]),'SUB':([47,48,50,51,52,53,54,56,62,71,89,90,91,92,93,95,96,97,107,108,131,],[-53,68,-46,-49,-52,-54,-55,68,68,68,-47,-48,-50,-51,-56,68,68,68,68,-7,68,]),'RAVNO':([47,50,51,52,53,54,62,89,90,91,92,93,108,],[-53,-46,-49,-52,-54,-55,78,-47,-48,-50,-51,-56,-7,]),'MORE':([47,50,51,52,53,54,62,89,90,91,92,93,108,],[-53,-46,-49,-52,-54,-55,79,-47,-48,-50,-51,-56,-7,]),'LESS':([47,50,51,52,53,54,62,89,90,91,92,93,108,],[-53,-46,-49,-52,-54,-55,80,-47,-48,-50,-51,-56,-7,]),'CONTINUE':([81,115,],[104,104,]),'BREAK':([81,115,],[105,105,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'dec_list':([2,45,117,],[3,65,130,]),'dec':([2,9,45,117,],[4,26,4,4,]),'id_list':([2,9,45,117,],[5,5,5,5,]),'def_list':([3,],[8,]),'def':([3,25,],[10,44,]),'stmt_list':([7,24,74,],[14,43,94,]),'stmt':([7,24,34,74,],[15,15,46,15,]),'assign':([7,24,34,74,81,106,115,129,130,],[16,16,16,16,100,119,100,119,119,]),'print':([7,24,34,74,81,106,115,129,130,],[17,17,17,17,101,120,101,120,120,]),'while':([7,24,34,74,81,106,115,129,130,],[18,18,18,18,102,121,102,121,121,]),'if':([7,24,34,74,81,106,115,129,130,],[19,19,19,19,103,122,103,122,122,]),'type':([12,],[28,]),'bool_exp':([22,23,39,],[37,42,61,]),'bool_exp_term':([22,23,39,59,],[38,38,38,75,]),'bool':([22,23,39,59,60,],[40,40,40,76,77,]),'exp':([35,36,41,55,78,79,80,84,124,],[48,56,62,71,95,96,97,107,131,]),'term':([35,36,41,55,67,68,78,79,80,84,124,],[50,50,50,50,89,90,50,50,50,50,50,]),'factor':([35,36,41,55,67,68,69,70,78,79,80,84,124,],[51,51,51,51,51,51,91,92,51,51,51,51,51,]),'defstmt':([35,36,41,55,67,68,69,70,78,79,80,84,124,],[52,52,52,52,52,52,52,52,52,52,52,52,52,]),'args':([66,],[85,]),'arg':([66,109,],[86,126,]),'stmt_list_if':([81,],[98,]),'stmt_if':([81,115,],[99,127,]),'stmt_list_def':([106,130,],[116,133,]),'stmt_def':([106,129,130,],[118,132,118,]),'return':([106,129,130,],[123,123,123,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> VAR dec_list OPEN_FIG stmt_list CLOSE_FIG','prog',5,'p_prog','Parser.py',24),
  ('prog -> VAR dec_list def_list OPEN_FIG stmt_list CLOSE_FIG','prog',6,'p_prog','Parser.py',25),
  ('def_list -> def','def_list',1,'p_def_list','Parser.py',32),
  ('def_list -> def_list SEMI_COLON def','def_list',3,'p_def_list','Parser.py',33),
  ('def -> DEF ID OPEN_PAREN dec_list CLOSE_PAREN OPEN_FIG stmt_list_def CLOSE_FIG','def',8,'p_def','Parser.py',40),
  ('def -> DEF ID OPEN_PAREN dec_list CLOSE_PAREN OPEN_FIG VAR dec_list stmt_list_def CLOSE_FIG','def',10,'p_def','Parser.py',41),
  ('defstmt -> ID OPEN_PAREN args CLOSE_PAREN','defstmt',4,'p_defstmt','Parser.py',48),
  ('args -> arg','args',1,'p_args','Parser.py',52),
  ('args -> args SEMI_COLON arg','args',3,'p_args','Parser.py',53),
  ('arg -> ID','arg',1,'p_arg','Parser.py',61),
  ('arg -> NUMBER_INT','arg',1,'p_arg','Parser.py',62),
  ('arg -> NUMBER_REAL','arg',1,'p_arg','Parser.py',63),
  ('arg -> OPEN_PAREN exp CLOSE_PAREN','arg',3,'p_arg','Parser.py',64),
  ('dec_list -> dec','dec_list',1,'p_dec_list','Parser.py',71),
  ('dec_list -> dec_list SEMI_COLON dec','dec_list',3,'p_dec_list','Parser.py',72),
  ('dec -> id_list DOUBLE_POINT type','dec',3,'p_dec','Parser.py',79),
  ('type -> INT','type',1,'p_type','Parser.py',83),
  ('type -> REAL','type',1,'p_type','Parser.py',84),
  ('type -> STRING','type',1,'p_type','Parser.py',85),
  ('id_list -> ID','id_list',1,'p_id_list','Parser.py',89),
  ('id_list -> id_list COMA ID','id_list',3,'p_id_list','Parser.py',90),
  ('stmt_list -> stmt','stmt_list',1,'p_stmt_list','Parser.py',97),
  ('stmt_list -> stmt_list SEMI_COLON stmt','stmt_list',3,'p_stmt_list','Parser.py',98),
  ('stmt -> assign','stmt',1,'p_stmt','Parser.py',105),
  ('stmt -> print','stmt',1,'p_stmt','Parser.py',106),
  ('stmt -> while','stmt',1,'p_stmt','Parser.py',107),
  ('stmt -> if','stmt',1,'p_stmt','Parser.py',108),
  ('stmt_list_if -> stmt_if','stmt_list_if',1,'p_stmt_list_if','Parser.py',113),
  ('stmt_list_if -> stmt_list_if SEMI_COLON stmt_if','stmt_list_if',3,'p_stmt_list_if','Parser.py',114),
  ('stmt_if -> assign','stmt_if',1,'p_stmt_if','Parser.py',121),
  ('stmt_if -> print','stmt_if',1,'p_stmt_if','Parser.py',122),
  ('stmt_if -> while','stmt_if',1,'p_stmt_if','Parser.py',123),
  ('stmt_if -> if','stmt_if',1,'p_stmt_if','Parser.py',124),
  ('stmt_if -> CONTINUE','stmt_if',1,'p_stmt_if','Parser.py',125),
  ('stmt_if -> BREAK','stmt_if',1,'p_stmt_if','Parser.py',126),
  ('stmt_list_def -> stmt_def','stmt_list_def',1,'p_stmt_list_def','Parser.py',131),
  ('stmt_list_def -> stmt_list_def SEMI_COLON stmt_def','stmt_list_def',3,'p_stmt_list_def','Parser.py',132),
  ('stmt_def -> assign','stmt_def',1,'p_stmt_def','Parser.py',139),
  ('stmt_def -> print','stmt_def',1,'p_stmt_def','Parser.py',140),
  ('stmt_def -> while','stmt_def',1,'p_stmt_def','Parser.py',141),
  ('stmt_def -> if','stmt_def',1,'p_stmt_def','Parser.py',142),
  ('stmt_def -> return','stmt_def',1,'p_stmt_def','Parser.py',143),
  ('return -> RETURN exp','return',2,'p_return','Parser.py',148),
  ('assign -> ID PRISV exp','assign',3,'p_assign','Parser.py',152),
  ('assign -> ID PRISV STRING','assign',3,'p_assign','Parser.py',153),
  ('exp -> term','exp',1,'p_exp','Parser.py',157),
  ('exp -> exp SUM term','exp',3,'p_exp','Parser.py',158),
  ('exp -> exp SUB term','exp',3,'p_exp','Parser.py',159),
  ('term -> factor','term',1,'p_term','Parser.py',166),
  ('term -> term MUL factor','term',3,'p_term','Parser.py',167),
  ('term -> term DIV factor','term',3,'p_term','Parser.py',168),
  ('factor -> defstmt','factor',1,'p_factor','Parser.py',175),
  ('factor -> ID','factor',1,'p_factor','Parser.py',176),
  ('factor -> NUMBER_INT','factor',1,'p_factor','Parser.py',177),
  ('factor -> NUMBER_REAL','factor',1,'p_factor','Parser.py',178),
  ('factor -> OPEN_PAREN exp CLOSE_PAREN','factor',3,'p_factor','Parser.py',179),
  ('print -> PRINT OPEN_PAREN exp CLOSE_PAREN','print',4,'p_print','Parser.py',185),
  ('print -> PRINT OPEN_PAREN STRING CLOSE_PAREN','print',4,'p_print','Parser.py',186),
  ('while -> WHILE bool_exp DO OPEN_FIG stmt_list CLOSE_FIG','while',6,'p_while','Parser.py',190),
  ('if -> IF bool_exp THEN OPEN_FIG stmt_list_if CLOSE_FIG','if',6,'p_if','Parser.py',194),
  ('bool_exp -> bool_exp OR bool_exp_term','bool_exp',3,'p_bool_exp','Parser.py',201),
  ('bool_exp -> bool_exp_term','bool_exp',1,'p_bool_exp','Parser.py',202),
  ('bool_exp -> NOT bool_exp','bool_exp',2,'p_bool_exp','Parser.py',203),
  ('bool_exp -> bool','bool_exp',1,'p_bool_exp','Parser.py',204),
  ('bool_exp_term -> bool_exp_term AND bool','bool_exp_term',3,'p_bool_exp_term','Parser.py',213),
  ('bool_exp_term -> bool','bool_exp_term',1,'p_bool_exp_term','Parser.py',214),
  ('bool -> OPEN_PAREN exp RAVNO exp CLOSE_PAREN','bool',5,'p_bool','Parser.py',223),
  ('bool -> OPEN_PAREN exp MORE exp CLOSE_PAREN','bool',5,'p_bool','Parser.py',224),
  ('bool -> OPEN_PAREN exp LESS exp CLOSE_PAREN','bool',5,'p_bool','Parser.py',225),
]
