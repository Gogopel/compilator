from ply import lex

reserved = {
        'def':'DEF',
        'return':'RETURN',
        'and':'AND',
        'or':'OR',
        'not':'NOT',
        'print':'PRINT',
        'while':'WHILE',
        'do':'DO',
        'if':'IF',
        'then':'THEN',
        'break':'BREAK',
        'continue':'CONTINUE',
        'int':'INT',
        'real':'REAL',
        'var':'VAR',
        'str':'STRING'
}

tokens = list(reserved.values()) + [
        'RAVNO',
        'DOUBLE_POINT',
        'COMA',
        'OPEN_PAREN',
        'CLOSE_PAREN',
        # Фигурные скобки
        'OPEN_FIG',
        'CLOSE_FIG',
        # Присваивание
        'PRISV',
        # Точка с запятой
        'SEMI_COLON',
        # Операторы
        'SUM',
        'SUB',
        'MUL',
        'DIV',
        # Больше - меньше
        'MORE',
        'LESS',
        # Числа int
        'NUMBER_INT',
        # Числа real
        'NUMBER_REAL',
        #Переменная
        'ID',
        ]

# Регулярные выражения для выделения лексем.
t_DOUBLE_POINT = r'\:'
t_RAVNO = r'\='
t_PRINT = r'print'
t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'
t_COMA = r'\,'
t_OPEN_FIG = r'\{'
t_CLOSE_FIG = r'\}'
t_PRISV = r'\:='
t_SEMI_COLON = r'\;'
t_SUM = r'\+'
t_SUB = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'
t_MORE = r'\>'
t_LESS = r'\<'
t_NUMBER_INT = r'\d+'
t_NUMBER_REAL = r'\d+\.\d+'
t_STRING = r'\"[^\'\n]*\"'

def t_comment(t):
    r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/'
    pass

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print ("Недопустимый символ '%s'" % t.value[0])

lex.lex()