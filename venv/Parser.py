import ply.yacc as yacc
from lexer import tokens
import sys

class Node:
    def parts_str(self):
        st = []
        for part in self.parts:
            st.append( str( part ) )
        return "\n".join(st)

    def __repr__(self):
        return self.type + ":\n\t" + self.parts_str().replace("\n", "\n\t")

    def add_parts(self, parts):
        self.parts += parts
        return self

    def __init__(self, type, parts):
        self.type = type
        self.parts = parts

def p_prog(p):
    '''prog : VAR dec_list OPEN_FIG stmt_list CLOSE_FIG
            | VAR dec_list def_list OPEN_FIG stmt_list CLOSE_FIG'''
    if len(p) == 6:
        p[0] = Node('prog', [p[2], p[4]])
    else:
        p[0] = Node('prog', [p[2], p[3], p[5]])

def p_def_list(p):
    '''def_list : def
               | def_list SEMI_COLON def'''
    if len(p) == 2:
        p[0] = Node('DEF', [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])

def p_def(p):
    '''def : DEF ID OPEN_PAREN dec_list CLOSE_PAREN OPEN_FIG stmt_list_def CLOSE_FIG
            | DEF ID OPEN_PAREN dec_list CLOSE_PAREN OPEN_FIG VAR dec_list stmt_list_def CLOSE_FIG'''
    if len(p) == 9:
        p[0] = Node(p[2], [p[4], p[7]])
    else:
        p[0] = Node(p[2], [p[4], p[8], p[9]])

def p_defstmt(p):
    '''defstmt : ID OPEN_PAREN args CLOSE_PAREN'''
    p[0] = Node(p[1], [p[3]])

def p_args(p):
    '''args : arg
            | args SEMI_COLON arg'''
    if len(p) == 2:
        p[0] = Node('args', [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])


def p_arg(p):
    '''arg : ID
            | NUMBER_INT
            | NUMBER_REAL
            | OPEN_PAREN exp CLOSE_PAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_dec_list(p):
    '''dec_list : dec
               | dec_list SEMI_COLON dec'''
    if len(p) == 2:
        p[0] = Node('VAR', [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])

def p_dec(p):
    '''dec : id_list DOUBLE_POINT type'''
    p[0] = Node('dec', [p[1], p[3]])

def p_type(p):
    '''type : INT
            | REAL
            | STRING'''
    p[0] = Node('type', [p[1]])

def p_id_list(p):
    '''id_list : ID
                | id_list COMA ID'''
    if len(p) == 2:
        p[0] = Node('Id', [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])

def p_stmt_list(p):
    '''stmt_list : stmt
                | stmt_list SEMI_COLON stmt'''
    if len(p) == 2:
        p[0] = Node('stmt', [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])

def p_stmt(p):
    '''stmt : assign
            | print
            | while
            | if'''
    if len(p) == 2:
        p[0] = p[1]

def p_stmt_list_if(p):
    '''stmt_list_if : stmt_if
                | stmt_list_if SEMI_COLON stmt_if'''
    if len(p) == 2:
        p[0] = Node('stmt', [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])

def p_stmt_if(p):
    '''stmt_if : assign
            | print
            | while
            | if
            | CONTINUE
            | BREAK'''
    if len(p) == 2:
        p[0] = p[1]

def p_stmt_list_def(p):
    '''stmt_list_def : stmt_def
                | stmt_list_def SEMI_COLON stmt_def'''
    if len(p) == 2:
        p[0] = Node('stmt', [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])

def p_stmt_def(p):
    '''stmt_def : assign
            | print
            | while
            | if
            | return'''
    if len(p) == 2:
        p[0] = p[1]

def p_return(p):
    '''return : RETURN exp'''
    p[0] = Node(p[1], [p[2]])

def p_assign(p):
    '''assign : ID PRISV exp
                | ID PRISV STRING'''
    p[0] = Node('assign', [p[1], p[3]])

def p_exp(p):
    '''exp : term
            | exp SUM term
            | exp SUB term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node(p[2], [p[1], p[3]])

def p_term(p):
    '''term : factor
            | term MUL factor
            | term DIV factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node(p[2], [p[1], p[3]])

def p_factor(p):
    '''factor : defstmt
            | ID
            | NUMBER_INT
            | NUMBER_REAL
            | OPEN_PAREN exp CLOSE_PAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else: p[0] = p[2]

def p_print(p):
    '''print : PRINT OPEN_PAREN exp CLOSE_PAREN
                | PRINT OPEN_PAREN STRING CLOSE_PAREN'''
    p[0] = Node('print', [p[3]])

def p_while(p):
    '''while : WHILE bool_exp DO OPEN_FIG stmt_list CLOSE_FIG'''
    p[0] = Node('while', [p[2], p[5]])

def p_if(p):
    '''if : IF bool_exp THEN OPEN_FIG stmt_list_if CLOSE_FIG'''
    if len(p) == 11:
        p[0] = Node('if', [p[2], p[5], p[9]])
    else:
        p[0] = Node('if', [p[2], p[5]])

def p_bool_exp(p):
    '''bool_exp : bool_exp OR bool_exp_term
                | bool_exp_term
                | NOT bool_exp
                | bool'''
    if len(p) == 4:
        p[0] = Node(p[2], [p[1], p[3]])
    elif len(p) == 3:
        p[0] = Node(p[1], [p[2]])
    else:
        p[0] = p[1]

def p_bool_exp_term(p):
    '''bool_exp_term : bool_exp_term AND bool
                | bool'''
    if len(p) == 4:
        p[0] = Node(p[2], [p[1], p[3]])
    elif len(p) == 3:
        p[0] = Node(p[1], [p[2]])
    else:
        p[0] = p[1]

def p_bool(p):
    '''bool : OPEN_PAREN exp RAVNO exp CLOSE_PAREN
            | OPEN_PAREN exp MORE exp CLOSE_PAREN
            | OPEN_PAREN exp LESS exp CLOSE_PAREN'''
    p[0] = Node(p[3], [p[2], p[4]])

def p_error(p):
    print ('Ошибка токена: ', p)
    sys.exit()

def obhod_for_table(result, table, functions):
    if (type(result) != Node):
        return
    elif (result.type == 'DEF'):
        for j in result.parts:
            if (len(j.parts) == 2):
                obhod_fun_for_table(j, j.type)
                functions.append(j.type)
            elif (len(j.parts) == 3):
                functions.append(j.type)
                for l in j.parts:
                    table = obhod_fun_for_table(l, j.type)
    elif (result.type == 'dec'):
        for i in result.parts[0].parts:
            table.append((i, result.parts[1].parts[0], 'main'))
        return
    else:
        for i in range(len(result.parts)):
            obhod_for_table(result.parts[i],table,functions)
    return table,functions


def obhod_fun_for_table(result, fun):
    if (type(result) != Node):
        return
    elif (result.type == 'dec'):
        for i in result.parts[0].parts:
            table.append((i, result.parts[1].parts[0], fun))
    else:
        for i in range(len(result.parts)):
            obhod_fun_for_table(result.parts[i], fun)
    return table


def edit_table(table):
    new_table = {}
    index_s = 0
    index_a = 0
    oblast='main'
    for i in table:
        new_table[i[0]] = []
        if i[2] == 'main':
            new_table[i[0]].append('s' + str(index_s))
            index_s = index_s + 1
        else:
            if (i[2] == oblast):
                new_table[i[0]].append('a' + str(index_a))
                index_a = index_a + 1
            else:
                index_a = 0
                new_table[i[0]].append('a' + str(index_a))
                index_a = index_a + 1
                oblast = i[2]
        new_table[i[0]].append(i[1])
        new_table[i[0]].append(i[2])
    return new_table


def check_scope(tree, name):
    if name.startswith('if') or (tree.isnumeric()) or (if_real(tree)):
        return True
    if (tree in table.keys()):
        if (table[tree][2] == name):
            return True
        else:
            print('Ошибка области видимости')
            print(tree + ' ' + name)
            sys.exit()
    else:
        print('Переменная ' + tree + ' не объявлена')
        sys.exit()

def global_obhod_for_tac(tree):
    if len(tree.parts) == 3:
        obhod_for_tac(tree.parts[0], 'main')
        obhod_for_tac(tree.parts[2], 'main')
        for funct in tree.parts[1].parts:
            tac[funct.type] = []
            obhod_for_tac(funct, funct.type)
    else:
        obhod_for_tac(tree.parts[0], 'main')
        obhod_for_tac(tree.parts[1], 'main')
    tac['main'].append('GOTO END')


def obhod_for_tac(tree, name):
    global j, if_count
    if (type(tree) != Node and (tree == 'break' or tree == 'continue')):
        tac[name].append(tree)
    elif (type(tree) != Node):
        return
    elif (tree.type == 'assign'):
        if (type(tree.parts[0]) == str and type(tree.parts[1]) == str):
            if (not check_scope(tree.parts[0], name)):
                return
            tac[name].append(':= ' + tree.parts[1] + ' ' + tree.parts[0])
        else:
            assign_obhod_for_tac(tree, name)
            if (not check_scope(tree.parts[0], name)):
                return
            tac[name].append(':= '+'t'+str(j-1)+ ' '+tree.parts[0])

            temp_tab['t'+str(j-1)]=[]
            temp_tab['t'+str(j-1)].append(tree.parts[0])
            j = 0

    elif (tree.type == 'if'):
        expression_obhod_for_tac(tree.parts[0], name)
        if_name = 'if'+str(if_count)
        if_count = if_count + 1
        tac[if_name] = []
        tac[name].append('IF ' + 't' + str(j - 1) + ' GOTO ' + if_name)
        obhod_for_tac(tree.parts[1], if_name)
        tac[if_name].append('GOTO after_if')
    elif (tree.type == 'while'):
        expression_obhod_for_tac(tree.parts[0], name)
        if_name = 'if'+str(if_count)
        if_count = if_count + 1
        tac[if_name] = []
        tac[name].append('IF ' + 't' + str(j - 1) + ' GOTO ' + if_name)
        obhod_for_tac(tree.parts[1], if_name)
        tac[if_name].append('GOTO start_if')
    elif (tree.type == 'return'):
        if (name == 'main'):
            print('ОШИБКА : у вас return не в функции')
        else:
            assign_obhod_for_tac(tree.parts[0],name)
            tac[name].append('return ' + 't'+str(j-1))
    elif (tree.type == 'print'):
        tac[name].append('print ' + tree.parts[0])

    else:
        for i in range(len(tree.parts)):
            obhod_for_tac(tree.parts[i], name)
    return tac

def assign_obhod_for_tac(tree, name):
    global j
    if type(tree) != Node:
        if (not check_scope(tree, name)):
            return
        return tree
    elif(tree.type == '*' or tree.type == '/' or tree.type == '+' or tree.type == '-'):
        operand = tree.type
        arg1 = assign_obhod_for_tac(tree.parts[0], name)
        arg2 = assign_obhod_for_tac(tree.parts[1], name)
        if arg1 == None and arg2 == None:
            arg1 = 't' + str(j - 2)
            temp_tab['t'+str(j-2)]=[]

            temp_tab['t' + str(j - 1)] = []
            temp_tab['t'+str(j-2)].append('t' + str(j - 1))
            temp_tab['t'+str(j-1)].append('t' + str(j - 2))
        if arg1 == None:
            arg1 = 't'+str(j-1)
            temp_tab['t'+str(j-1)]=[]
            temp_tab['t'+str(j-1)].append(arg2)
        if arg2 == None:
            arg2 = 't'+str(j-1)
            temp_tab['t'+str(j-1)].append(arg1)
        else:
            temp_tab['t'+str(j)] = []
            temp_tab['t'+str(j)].append(arg1)
        temp = 't'+str(j)
        j = j+1
        tac[name].append(str(operand) + ' ' + str(arg1) + ' ' + str(arg2) + ' ' + str(temp))
    elif (tree.type in functions):
        string = 'Call ' + tree.type + ' '
        for arg in tree.parts[0].parts:
            string = string + arg + ' '
        temp = 't' + str(j)
        j = j + 1
        string = string + temp
        tac[name].append(string)
    else:
        for i in range(len(tree.parts)):
            assign_obhod_for_tac(tree.parts[i], name)

def expression_obhod_for_tac(tree, name):
    global j
    if type(tree) != Node:
        if (not check_scope(tree, name)):
            return
        return tree
    elif(tree.type == 'and' or tree.type == 'or'):
        operand = tree.type
        arg1 = expression_obhod_for_tac(tree.parts[0], name)
        arg2 = expression_obhod_for_tac(tree.parts[1], name)
        if arg1 == None and arg2 == None:
            arg1 = 't' + str(j - 2)
            arg2 = 't' + str(j - 1)
        if arg1 == None:
            arg1 = 't'+str(j-1)
            temp_tab['t' + str(j - 1)].append(arg2)
        if arg2 == None:
            arg2 = 't'+str(j-1)
            temp_tab['t' + str(j - 1)].append(arg1)
        temp = 't'+str(j)
        if not(temp in temp_tab):
            temp_tab[temp]=[]
            temp_tab['t' + str(j)].append(arg1)
        j = j+1
        tac[name].append(str(operand) + ' ' + str(arg1) + ' ' + str(arg2) + ' ' + str(temp))
    elif (tree.type == 'not'):
        operand = tree.type
        expression_obhod_for_tac(tree.parts[0], name)
        arg = 't'+str(j-1)
        temp = 't' + str(j)
        j = j + 1
        tac[name].append(str(operand) + ' ' + str(arg) + ' ' + str(temp))
    elif (tree.type == '>' or tree.type == '<' or tree.type == '='):
        operand = tree.type
        arg1 = assign_obhod_for_tac(tree.parts[0], name)
        arg2 = assign_obhod_for_tac(tree.parts[1], name)
        temp = 't' + str(j)
        temp_tab[temp]=[]
        temp_tab[temp].append(arg1)
        j = j + 1
        tac[name].append(str(operand) + ' ' + str(arg1) + ' ' + str(arg2) + ' ' + str(temp))
    else:
        for i in range(len(tree.parts)):
            expression_obhod_for_tac(tree.parts[i], name)

def if_real(string):
    try:
        float(string)
        if (string.isnumeric()):
            return False
        return True
    except ValueError:
        return False

def asm(tac, table):
    if_count = 0
    skip_count = 0
    flag = False
    f_bc = False
    str_count = 0
    data = ''
    file = open('out.s', 'w')
    data = data + '.data\n\ttrue: .byte 1\n\tfalse: .byte 0\n'
    file.write('.text\n')
    for i in range (len(temp_tab)):
        if temp_tab['t'+str(i)][0].isnumeric():
            temp_tab['t'+str(i)]=[]
            temp_tab['t' + str(i)] = 'int'
            table['t' + str(i)] = []
            table['t' + str(i)] = 'int'
        elif if_real(temp_tab['t'+str(i)][0]):
            temp_tab['t'+str(i)]=[]
            temp_tab['t' + str(i)] = 'real'
            temp_real_tab['f'+ str(i)]=[]
            temp_real_tab['f'+ str(i)].append('real')
            table['t' + str(i)] = []
            table['t' + str(i)] = 'real'
        elif temp_tab['t'+str(i)][0] in table and table[temp_tab['t'+str(i)][0]][1]=='int':
            temp_tab['t' + str(i)] = []
            temp_tab['t' + str(i)] = 'int'
            table['t' + str(i)] = []
            table['t' + str(i)] = 'int'
        elif temp_tab['t'+str(i)][0] in table and table[temp_tab['t'+str(i)][0]][1]=='real':
            temp_tab['t'+str(i)]=[]
            temp_tab['t' + str(i)] = 'real'
            temp_real_tab['f'+ str(i)]=[]
            temp_real_tab['f'+ str(i)].append('real')
            table['t' + str(i)] = []
            table['t' + str(i)] = 'real'
        else:
            temp_tab['t' + str(i)] = []
            temp_tab['t' + str(i)] = 'int'
            table['t' + str(i)] = []
            table['t' + str(i)] = 'int'
    for i in (table):
        if i==('t0') :
            break
        temp_tab[i]=[]
        temp_tab[i].append(i)
    for label in tac:
        file.write(label + ':\n')
        for command in tac[label]:
            command_lst = command.split(' ')
            if ( command_lst[0] == ':=' ):
                if command_lst[1].isnumeric() and (table[command_lst[2]][1] == 'int' or temp_tab[command_lst[2]][0]=='i'):
                    if (command_lst[2] in temp_tab.keys() and temp_tab[command_lst[2]][0]!=command_lst[2]):
                        file.write('\tli $' + command_lst[2] + ', ' + command_lst[1] + '\n')
                    else:
                        file.write('\tli $' + table[command_lst[2]][0] + ', ' + command_lst[1] + '\n')
                elif (if_real(command_lst[1]) and (table[command_lst[2]][1] == 'real' or temp_tab[command_lst[2]][0]=='r')):
                    data=data + '\tdrob'+ command_lst[1] +': .float '+command_lst[1]+'\n'
                    if (command_lst[2] in temp_tab.keys() and temp_tab[command_lst[2]][0]!=command_lst[2]):
                        file.write('\tla $' + command_lst[2] + ', drob' + command_lst[1] + '\n')
                    else:
                        file.write('\tla $' + table[command_lst[2]][0] + ', drob' + command_lst[1] + '\n')
                elif command_lst[1].startswith('\"') and command_lst[1].endswith('\"') and (table[command_lst[2]][1] == 'str'):
                    data = data + '\t' + command_lst[2] + ': .asciiz ' + command_lst[1] +'\n'

                elif(command_lst[1] in table.keys() ):
                    if (command_lst[1] in temp_tab.keys() and temp_tab[command_lst[1]][0]!=command_lst[1]):
                        if (command_lst[2] in temp_tab.keys() and temp_tab[command_lst[2]][0]!=command_lst[2]):
                            if temp_tab[command_lst[1]][0]=='r':

                                file.write('\tmov.s $f' +  command_lst[2][1:] + ', $f' + command_lst[1][1:] + '\n')
                            else:
                                file.write('\tmove $' + command_lst[2] + ', $f' + command_lst[1] + '\n')
                        elif command_lst[2] in table.keys():
                            if temp_tab[command_lst[1]][0] == 'r':

                                file.write('\tmov.s $' + table[command_lst[2]][0] + ', $f' + command_lst[1][1:] + '\n')
                            else:
                                file.write('\tmove $' + table[command_lst[2]][0] + ', $' + command_lst[1] + '\n')
                    elif (command_lst[1] in table.keys()):
                        if (command_lst[2] in table.keys()):
                            if table[command_lst[2]][1] =='real':
                                file.write('\tmov.s $' + table[command_lst[2]][0] + ', $' + table[command_lst[1]][0] + '\n')
                            else:
                                file.write('\tmove $' + table[command_lst[2]][0] + ', $' + table[command_lst[1]][0] + '\n')



                else:
                    if (command_lst[2] in table.keys()):
                        file.write('\tmove $' + command_lst[2] + ', $' + command_lst[1] + '\n')
                    elif (command_lst[2] in table.keys()):
                        file.write('\tmove $' + table[command_lst[2]][0] + ', $' + command_lst[1] +'\n')
                    else:
                        file.write('\tmove $' + command_lst[2] + ', $' + command_lst[1] + '\n')

            elif ( command_lst[0] == '*' ):
                if not(if_real(command_lst[1]) or if_real(command_lst[2])):
                        if(command_lst[1].isnumeric() or table[command_lst[1]][1]=='int' or temp_tab[command_lst[1]][0]=='i') and (command_lst[2].isnumeric() or table[command_lst[2]][1]=='int'or temp_tab[command_lst[2]][0]=='i'):

                            if command_lst[1].isnumeric():
                                file.write('\tli $t0, '+ command_lst[1] + '\n')
                                arg1 = '$t0'
                                if command_lst[2].isnumeric():
                                    file.write('\tli $t1, '+ command_lst[2]+ '\n')
                                    arg2 = '$t1'
                                    file.write('\tmult ' + arg1 + ', ' + arg2 + '\n')
                                elif(command_lst[2] in table and table[command_lst[2]][1]=='int'):
                                    arg2 = '$'+ table[command_lst[2]][0]
                                    file.write('\tmult ' + arg1 + ', ' + arg2 + '\n')
                                elif (temp_tab[command_lst[2]][0] == 'i'):
                                    arg2 = '$' + command_lst[2]
                                    file.write('\tmult ' + arg1 + ', ' + arg2 + '\n')
                            elif ((command_lst[1] in table and table[command_lst[1]][1] == 'int')or(temp_tab[command_lst[1]][0] == 'i' and command_lst[1] in temp_tab)):
                                if (command_lst[1] in table and table[command_lst[1]][1] == 'int'):
                                    arg1 = '$' + table[command_lst[1]][0]
                                else:
                                    arg1 = '$' + command_lst[1]
                                if command_lst[2].isnumeric():
                                    file.write('\tli $t1, '+ command_lst[2]+ '\n')
                                    arg2 = '$t1'
                                    file.write('\tmult ' + arg1 + ', ' + arg2 + '\n')
                                elif (command_lst[2] in table and table[command_lst[2]][1] == 'int'):
                                    arg2 = '$' + table[command_lst[2]][0]
                                    file.write('\tmult ' + arg1 + ', ' + arg2 + '\n')
                                elif (temp_tab[command_lst[2]][0] == 'i' and command_lst[2] in temp_tab):
                                    arg2 = '$' + command_lst[2]
                                    file.write('\tmult ' + arg1 + ', ' + arg2 + '\n')
                                file.write('\tmflo $' + command_lst[3] + '\n')
                        elif ((command_lst[1] in table and table[command_lst[1]][1] == 'real') or (temp_tab[command_lst[1]][0] == 'r' and command_lst[1] in temp_tab)):
                            if (command_lst[1] in table and table[command_lst[1]][1] == 'real'):
                                arg1 = '$' + table[command_lst[1]][0]
                            else:
                                chislo = command_lst[1][1:]
                                arg1 = '$f' + str(chislo)
                            if if_real(command_lst[2]):
                                file.write('\tli.s $f1, ' + command_lst[2] + '\n')
                                arg2 = '$f1'
                                file.write('\tmul.s $f' + command_lst[3][1:] + ', ' + arg1 + ', ' + arg2 + '\n')
                            elif (command_lst[2] in table and table[command_lst[2]][1] == 'real'):
                                arg2 = '$' + table[command_lst[2]][0]
                                file.write('\tli.s $f' + str(chislo) + ', ' + arg1 + ', ' + arg2 + '\n')
                                chislo = command_lst[3][1:]
                                file.write('\tmul.s $f' + str(chislo) + ', ' + arg1 + ', ' + arg2 + '\n')
                            elif (temp_tab[command_lst[2]][0] == 'r' and command_lst[2] in temp_tab):
                                chislo = command_lst[2][1:]
                                arg2 = '$f' + str(chislo)
                                file.write('\tmul.s $f' + command_lst[3][1:] + ', ' + arg1 + ', ' + arg2 + '\n')
                            else:
                                print('error неверный тип')
                                return
                elif if_real(command_lst[1]):
                    file.write('\tli.s $f0, ' + command_lst[1] + '\n')
                    arg1 = '$f0'
                    if if_real(command_lst[2]):
                        file.write('\tli.s $f1, ' + command_lst[2] + '\n')
                        arg2 = '$f1'
                        file.write('\tmul.s $f'+ command_lst[3][1:]+', '  + arg1 + ', ' + arg2 + '\n')
                    elif (command_lst[2] in table and table[command_lst[2]][1] == 'real'):
                        arg2 = '$' + table[command_lst[2]][0]
                        file.write('\tmul.s $f'+ command_lst[3][1:]+', ' + arg1 + ', ' + arg2 + '\n')
                    elif (temp_tab[command_lst[2]][0] == 'r' and command_lst[2] in temp_tab):
                        chislo = command_lst[2][1:]
                        arg2 = '$f' +str(chislo)
                        file.write('\tmul.s $f'+ command_lst[3][1:]+', '  + arg1 + ', ' + arg2 + '\n')
                    else:
                        print('error неверный тип')
                        return
            elif ( command_lst[0] == '/' ):
                if not(if_real(command_lst[1]) or if_real(command_lst[2])):
                        if(command_lst[1].isnumeric() or table[command_lst[1]][1]=='int' or temp_tab[command_lst[1]][0]=='i') and (command_lst[2].isnumeric() or table[command_lst[2]][1]=='int' or temp_tab[command_lst[1]][0]=='i'):
                            if command_lst[1].isnumeric():
                                file.write('\tli $t0, '+ command_lst[1] + '\n')
                                arg1 = '$t0'
                                if command_lst[2].isnumeric():
                                    file.write('\tli $t1, '+ command_lst[2]+ '\n')
                                    arg2 = '$t1'
                                    file.write('\tdiv ' + arg1 + ', ' + arg2 + '\n')
                                elif(command_lst[2] in table and table[command_lst[2]][1]=='int'):
                                    arg2 = '$'+table[command_lst[2]][0]
                                    file.write('\tdiv ' + arg1 + ', ' + arg2 + '\n')
                                elif (temp_tab[command_lst[2]][0] == 'i'):
                                    arg2 = '$' + command_lst[2]
                                    file.write('\tdiv ' + arg1 + ', ' + arg2 + '\n')
                            elif((command_lst[1] in table and table[command_lst[1]][1]=='int')or( temp_tab[command_lst[1]][0]=='i' and command_lst[1] in temp_tab)):
                                if (command_lst[1] in table and table[command_lst[1]][1]=='int' ):
                                    arg1 = '$' + table[command_lst[1]][0]
                                else:
                                    arg1 = '$' + command_lst[1]
                                if command_lst[2].isnumeric():
                                    file.write('\tli $t1, '+ command_lst[2]+ '\n')
                                    arg2 = '$t1'
                                    file.write('\tdiv ' + arg1 + ', ' + arg2 + '\n')
                                elif (command_lst[2] in table and table[command_lst[2]][1] == 'int'):
                                    arg2 = '$' + table[command_lst[2]][0]
                                    file.write('\tdiv ' + arg1 + ', ' + arg2 + '\n')
                                elif (temp_tab[command_lst[2]][0] == 'i' and command_lst[2] in temp_tab):
                                    arg1 = '$' + command_lst[2]
                                    file.write('\tdiv ' + arg1 + ', ' + arg2 + '\n')
                            file.write('\tmflo $' + command_lst[3] + '\n')
                        elif ((command_lst[1] in table and table[command_lst[1]][1] == 'real') or (
                                temp_tab[command_lst[1]][0] == 'r' and command_lst[1] in temp_tab)):
                            if (command_lst[1] in table and table[command_lst[1]][1] == 'real'):
                                arg1 = '$' + table[command_lst[1]][0]
                            else:
                                arg1 = '$f' + command_lst[1][1:]
                            if if_real(command_lst[2]):
                                file.write('\tli.s $f1, ' + command_lst[2] + '\n')
                                arg2 = '$f1'
                                file.write('\tdiv.s $f' + command_lst[3][1:] + ', ' + arg1 + ', ' + arg2 + '\n')
                            elif (command_lst[2] in table and table[command_lst[2]][1] == 'real'):
                                arg2 = '$' + table[command_lst[2]][0]
                                file.write('\tdiv.s $f' + command_lst[3][1:] + ', ' + arg1 + ', ' + arg2 + '\n')
                            elif (temp_tab[command_lst[2]][0] == 'r' and command_lst[2] in temp_tab):
                                arg2 = '$f' + command_lst[2][1:]
                                file.write('\tdiv.s $f' + command_lst[3][1:] + ', ' + arg1 + ', ' + arg2 + '\n')
                        else:
                            print('error неверный тип')
                            return
                elif if_real(command_lst[1]):
                    file.write('\tli.s $f0, ' + command_lst[1] + '\n')
                    arg1 = '$f0'
                    if if_real(command_lst[2]):
                        file.write('\tli.s $f1, ' + command_lst[2] + '\n')
                        arg2 = '$f1'
                        file.write('\tdiv.s $f'  + command_lst[3][1:]+', '+ arg1 + ', ' + arg2 + '\n')
                    elif (command_lst[2] in table and table[command_lst[2]][1] == 'real'):
                        arg2 = '$' + table[command_lst[2]][0]
                        file.write('\tdiv.s $f' + command_lst[3][1:]+', ' + arg1 + ', ' + arg2 + '\n')
                    elif (temp_tab[command_lst[2]][0] == 'r' and command_lst[2] in temp_tab):
                        arg2 = '$f' + command_lst[2][1:]
                        file.write('\tdiv.s $f' + command_lst[3][1:]+', ' + arg1 + ', ' + arg2 + '\n')
                    else:
                        print('error неверный тип')
                        return
                elif ((command_lst[1] in table and table[command_lst[1]][1] == 'real') or ( temp_tab[command_lst[1]][0]=='r' and command_lst[1] in temp_tab)):
                    if (command_lst[1] in table and table[command_lst[1]][1] == 'real'):
                        arg1 = '$' + table[command_lst[1]][0]
                    else:
                        arg1 = '$f' + command_lst[1][1:]
                    if if_real(command_lst[2]):
                        file.write('\tli.s $f1, ' + command_lst[2] + '\n')
                        arg2 = '$f1'
                        file.write('\tdiv.s $f' + command_lst[3][1:]+', ' + arg1 + ', ' + arg2 + '\n')
                    elif (command_lst[2] in table and table[command_lst[2]][1] == 'real'):
                        arg2 = '$' + table[command_lst[2]][0]
                        file.write('\tdiv.s $f' + command_lst[3][1:]+', ' + arg1 + ', ' + arg2 + '\n')
                    elif (temp_tab[command_lst[2]][0] == 'r' and command_lst[2] in temp_tab):
                        arg2 = '$f' + command_lst[2][1:]
                        file.write('\tdiv.s $f' + command_lst[3][1:]+', ' + arg1 + ', ' + arg2 + '\n')
                else:
                    print('error неверный тип')
                    return
            elif (command_lst[0] == '+'):
                if not(if_real(command_lst[1]) or if_real(command_lst[2])):
                        if(command_lst[1].isnumeric() or table[command_lst[1]][1]=='int' or temp_tab[command_lst[1]][0]=='i') and (command_lst[2].isnumeric() or table[command_lst[2]][1]=='int' or temp_tab[command_lst[2]][0]=='i'):
                            if command_lst[1].isnumeric():
                                file.write('\tli $t0, '+ command_lst[1] + '\n')
                                arg1 = '$t0'
                                if command_lst[2].isnumeric():
                                    file.write('\tli $t1, '+ command_lst[2]+ '\n')
                                    arg2 = '$t1'
                                    file.write('\taddu $'+ command_lst[3] +', '+ arg1 + ', ' + arg2 + '\n')
                                elif(command_lst[2] in table and table[command_lst[2]][1]=='int'):
                                    arg2 = '$'+table[command_lst[2]][0]
                                    file.write('\taddu $'+ command_lst[3] +', ' + arg1 + ', ' + arg2 + '\n')
                                elif(temp_tab[command_lst[2]][0]=='i'):
                                    arg2 = '$'+command_lst[2]
                                    file.write('\taddu $' + command_lst[3] + ', ' + arg1 + ', ' + arg2 + '\n')
                            elif((command_lst[1] in table and table[command_lst[1]][1]=='int' )or( temp_tab[command_lst[1]][0]=='i' and command_lst[1] in temp_tab)):
                                if (command_lst[1] in table and table[command_lst[1]][1]=='int' ):
                                    arg1 = '$' + table[command_lst[1]][0]
                                else:
                                    arg1 = '$' + command_lst[1]
                                if command_lst[2].isnumeric():
                                    file.write('\tli $t1, '+ command_lst[2]+ '\n')
                                    arg2 = '$t1'
                                    file.write('\taddu $' + command_lst[3] + ', ' + arg1 + ', ' + arg2 + '\n')
                                elif (command_lst[2] in table and table[command_lst[2]][1] == 'int'):
                                    arg2 = '$' + table[command_lst[2]][0]
                                    file.write('\taddu $' + command_lst[3] + ', ' + arg1 + ', ' + arg2 + '\n')
                                elif( temp_tab[command_lst[2]][0]=='i' and command_lst[2] in temp_tab):
                                    arg2 = '$' + command_lst[2]
                                    file.write('\taddu $' + command_lst[3] + ', ' + arg1 + ', ' + arg2 + '\n')
                        elif ((command_lst[1] in table and table[command_lst[1]][1] == 'real') or (
                                temp_tab[command_lst[1]][0] == 'r' and command_lst[1] in temp_tab)):
                            if (command_lst[1] in table and table[command_lst[1]][1] == 'real'):
                                arg1 = '$' + table[command_lst[1]][0]
                            else:
                                arg1 = '$f' + command_lst[1][1:]
                            if if_real(command_lst[2]):
                                file.write('\tli.s $f1, ' + command_lst[2] + '\n')
                                arg2 = '$f1'
                                file.write('\tadd.s $f' + command_lst[3][1:] + ', ' + arg1 + ', ' + arg2 + '\n')
                            elif (command_lst[2] in table and table[command_lst[2]][1] == 'real'):
                                arg2 = '$' + table[command_lst[2]][0]
                                file.write('\tadd.s $f' + command_lst[3][1:] + ', ' + arg1 + ', ' + arg2 + '\n')
                            elif (temp_tab[command_lst[2]][0] == 'r' and command_lst[2] in temp_tab):
                                arg2 = '$f' + command_lst[2][1:]
                                file.write('\tadd.s $f' + command_lst[3][1:] + ', ' + arg1 + ', ' + arg2 + '\n')
                        else:
                            print('error неверный тип')
                            return
                elif if_real(command_lst[1]):
                    file.write('\tli.s $f0, ' + command_lst[1] + '\n')
                    arg1 = '$f0'
                    if if_real(command_lst[2]):
                        file.write('\tli.s $f1, ' + command_lst[2] + '\n')
                        arg2 = '$f1'
                        file.write('\tadd.s $f'+ command_lst[3][1:] +', ' + arg1 + ', ' + arg2 + '\n')
                    elif ((command_lst[2] in table and table[command_lst[2]][1] == 'real') or ( temp_tab[command_lst[1]][0]=='r' and command_lst[1] in temp_tab)):
                        if (command_lst[2] in table and table[command_lst[2]][1] == 'real'):
                            arg2 = '$' + table[command_lst[2]][0]
                        elif (temp_tab[command_lst[1]][0]=='r' and command_lst[1] in temp_tab):
                            arg2 = '$' + command_lst[2]
                        file.write('\tadd.s $f' + command_lst[3][1:] + ', ' + arg1 + ', ' + arg2 + '\n')
                    else:
                        print('error неверный тип')
                        return
                else:
                    print('error неверный тип')
                    return
            elif (command_lst[0] == '-'):
                if not(if_real(command_lst[1]) or if_real(command_lst[2])):
                        if(command_lst[1].isnumeric() or table[command_lst[1]][1]=='int' or temp_tab[command_lst[1]][0]=='i') and (command_lst[2].isnumeric() or table[command_lst[2]][1]=='int' or  temp_tab[command_lst[1]][0]=='i'):
                            if command_lst[1].isnumeric():
                                file.write('\tli $t0, '+ command_lst[1] + '\n')
                                arg1 = '$t0'
                                if command_lst[2].isnumeric():
                                    file.write('\tli $t1, '+ command_lst[2]+ '\n')
                                    arg2 = '$t1'
                                    file.write('\tsubu $'+ command_lst[3] +', '+ arg1 + ', ' + arg2 + '\n')
                                elif(command_lst[2] in table and table[command_lst[2]][1]=='int'):
                                    arg2 = '$'+table[command_lst[2]][0]
                                    file.write('\tsubu $'+ command_lst[3] +', ' + arg1 + ', ' + arg2 + '\n')
                                elif(temp_tab[command_lst[2]][0]=='i'):
                                    arg2 = '$'+command_lst[2]
                                    file.write('\tsubu $' + command_lst[3] + ', ' + arg1 + ', ' + arg2 + '\n')
                            elif((command_lst[1] in table and table[command_lst[1]][1]=='int')or ( temp_tab[command_lst[1]][0]=='i' and command_lst[1] in temp_tab)):
                                if (command_lst[1] in table and table[command_lst[1]][1] == 'int'):
                                    arg1 = '$' + table[command_lst[1]][0]
                                else:
                                    arg1 = '$' + command_lst[1]
                                if command_lst[2].isnumeric():
                                    file.write('\tli $t1, '+ command_lst[2]+ '\n')
                                    arg2 = '$t1'
                                    file.write('\tsubu $' + command_lst[3] + ', ' + arg1 + ', ' + arg2 + '\n')
                                elif (command_lst[2] in table and table[command_lst[2]][1] == 'int'):
                                    arg2 = '$' + table[command_lst[2]][0]
                                    file.write('\tsubu $' + command_lst[3] + ', ' + arg1 + ', ' + arg2 + '\n')
                                elif (temp_tab[command_lst[2]][0] == 'i' and command_lst[2] in temp_tab):
                                    arg2 = '$' + command_lst[2]
                                    file.write('\tsubu $' + command_lst[3] + ', ' + arg1 + ', ' + arg2 + '\n')
                        elif ((command_lst[1] in table and table[command_lst[1]][1] == 'real') or (
                                temp_tab[command_lst[1]][0] == 'r' and command_lst[1] in temp_tab)):
                            if (command_lst[1] in table and table[command_lst[1]][1] == 'real'):
                                arg1 = '$' + table[command_lst[1]][0]
                            else:
                                arg1 = '$f' + command_lst[1][1:]
                            if if_real(command_lst[2]):
                                file.write('\tli.s $f1, ' + command_lst[2] + '\n')
                                arg2 = '$f1'
                                file.write('\tsubu.s $f' + command_lst[3][1:] + ', ' + arg1 + ', ' + arg2 + '\n')
                            elif (command_lst[2] in table and table[command_lst[2]][1] == 'real'):
                                arg2 = '$' + table[command_lst[2]][0]
                                file.write('\tsubu.s $f' + command_lst[3][1:] + ', ' + arg1 + ', ' + arg2 + '\n')
                            elif (temp_tab[command_lst[2]][0] == 'r' and command_lst[2] in temp_tab):
                                arg2 = '$f' + command_lst[2][1:]
                                file.write('\tsubu.s $f' + command_lst[3][1:] + ', ' + arg1 + ', ' + arg2 + '\n')
                        else:
                            print('error неверный тип')
                            return
                elif if_real(command_lst[1]):
                    file.write('\tli.s $f0, ' + command_lst[1] + '\n')
                    arg1 = '$f0'
                    if if_real(command_lst[2]):
                        file.write('\tli.s $f1, ' + command_lst[2] + '\n')
                        arg2 = '$f1'
                        file.write('\tsubu.s $f'+ command_lst[3][1:] +', ' + arg1 + ', ' + arg2 + '\n')
                    elif ((command_lst[2] in table and table[command_lst[2]][1] == 'real') or (temp_tab[command_lst[2]][0]=='r' and command_lst[2] in temp_tab)):
                        if (command_lst[1] in table and table[command_lst[1]][1] == 'real'):
                            arg2 = '$' + table[command_lst[2]][0]
                        else:
                            arg2 = '$f' + command_lst[2][1:]
                        file.write('\tsubu.s $' + command_lst[3][1:] + ', ' + arg1 + ', ' + arg2 + '\n')
                    else:
                        print('error неверный тип')
                        return
                else:
                    print('error неверный тип')
                    return
            elif (command_lst[0] == '<' or command_lst[0] == '>'
                    or command_lst[0] == '='):
                if flag == False:
                    L = 'L' + str(if_count)
                    if_count = if_count + 1
                    flag = True
                    file.write(L + ':\n')
                if command_lst[0] == '<':
                    file.write('\tla $' + command_lst[3] + ', false\n')
                    file.write('\tbge $' + table[command_lst[1]][0] + ', $' + table[command_lst[2]][0] + ', SKIP'+str(skip_count) + '\n')
                    file.write('\tla $' + command_lst[3] + ', true\n')
                    file.write('SKIP'+str(skip_count) + ':\n')
                    skip_count = skip_count + 1
                elif command_lst[0] == '>':
                    file.write('\tla $' + command_lst[3] + ', false\n')
                    file.write('\tble $' + table[command_lst[1]][0] + ', $' + table[command_lst[2]][0] + ', SKIP'+str(skip_count) + '\n')
                    file.write('\tla $' + command_lst[3] + ', true\n')
                    file.write('SKIP'+str(skip_count) + ':\n')
                    skip_count = skip_count + 1
                elif command_lst[0] == '=':
                    file.write('\tla $' + command_lst[3] + ', false\n')
                    file.write('\tbne $' + table[command_lst[1]][0] + ', $' + table[command_lst[2]][0] + ', SKIP'+str(skip_count) + '\n')
                    file.write('\tla $' + command_lst[3] + ', true\n')
                    file.write('SKIP'+str(skip_count) + ':\n')
                    skip_count = skip_count + 1
            elif (command_lst[0] == 'and' or command_lst[0] == 'or'):
                file.write('\t' + command_lst[0] + ' $' + command_lst[3] + ', $' + command_lst[1] + ', $' + command_lst[2] + '\n')
            elif (command_lst[0] == 'not'):
                index = command_lst[2][1:]
                index = int(index) + 1
                temp = 't' + str(index)
                file.write('\tla $' + temp + ' false\n')
                file.write('\tnor $' + command_lst[2] + ', $' + command_lst[1] + ', $' + temp + '\n')
            elif (command_lst[0] == 'IF'):
                flag = False
                index = command_lst[1][1:]
                index = int(index) + 1
                temp = 't' + str(index)
                file.write('\tla $' + temp + ', true\n')
                file.write('\tbeq $' + temp + ', $' + command_lst[1] + ', ' + command_lst[3] + '\n')
                file.write('L' + str(if_count) + ':\n')
                if_count = if_count + 1
            elif (command_lst[0] == 'GOTO'):
                if (command_lst[1] == 'after_if'):
                    if f_bc == False:
                        file.write('\tj L' + str(if_count - 1) + '\n')
                elif (command_lst[1] == 'start_if'):
                    file.write('\tj L' + str(if_count - 2) + '\n')
                else:
                    file.write('\tj ' + command_lst[1] + '\n')
            elif (command_lst[0] == 'break'):
                file.write('\tj L' + str(if_count - 3) + '\n')
                f_bc = True
            elif (command_lst[0] == 'continue'):
                file.write('\tj L' + str(if_count - 4) + '\n')
                f_bc = True
            elif (command_lst[0] == 'print'):
                if (command_lst[1].startswith('\"') and command_lst[1].endswith('\"')):
                    data=data +'\tstr'+str(str_count) + ': .asciiz '+command_lst[1]+'\n'
                    str_count = str_count+1
                    file.write('\tli $v0, 4\n')
                    file.write('\tla $a0, '+'str'+str(str_count-1)+'\n')
                    file.write('\tsyscall\n')
                elif (command_lst[1] in table and table[command_lst[1]][1] == 'str'):
                    file.write('\tli $v0, 4\n')
                    file.write('\tla $a0, ' + command_lst[1] + '\n')
                    file.write('\tsyscall\n')
                elif (command_lst[1].isnumeric()):
                    file.write('\tli $v0, 1\n')
                    file.write('\tla $a0, '+command_lst[1] + '\n')
                    file.write('\tsyscall\n')
                elif (if_real(command_lst[1])):
                    data=data+'\tdrob'+ command_lst[1] +': .float '+command_lst[1]+'\n'
                    file.write('\tli $v0, 2\n')
                    file.write('\tlwc1 $f14, drob' + command_lst[1] + '\n')
                    file.write('\tsyscall\n')
                elif (command_lst[1] in table and table[command_lst[1]][1] == 'int'):
                    file.write('\tli $v0, 1\n')
                    file.write('\tla $a0, ' + '($' + table[command_lst[1]][0] + ')\n')
                    file.write('\tsyscall\n')
                elif (command_lst[1] in table and table[command_lst[1]][1] == 'real'):
                    file.write('\tli $v0, 2\n')
                    file.write('\tlwc1 $f12, ($' + table[command_lst[1]][0] + ')\n')
                    file.write('\tsyscall\n')
            elif (command_lst[0] == 'return'):
                file.write('\tmove $t9, $' + command_lst[1] + '\n' )
                file.write('\tjr $ra\n')
            elif (command_lst[0] == 'Call'):
                args = command_lst[2:len(command_lst)-1]
                for i in range(len(args)):
                    file.write('\tmove $a' + str(i) + ', $' + table[args[i]][0] + '\n')
                file.write('\tjal ' + command_lst[1] + '\n')
                file.write('\tmove $' + command_lst[len(command_lst)-1] + ', $t9\n')
    file.write('END:\n')
    file.close()
    file = open('out.s', 'r')
    text = file.read()
    file.close()
    file = open('out.s', 'w')
    file.write(data)
    file.write(text)
    file.close()
if __name__ == '__main__':

    file = open('code.txt', 'r')
    text_input = file.read()
    file.close()
    parser = yacc.yacc()
    result = parser.parse(text_input)
    print('__________AST__________')
    print(result)
    table = []
    temp_tab = {}
    functions = []
    table,functions = obhod_for_table(result,table,functions)
    table = edit_table(table)
    print('__________SymTab__________')
    for key in table:
        print(key + ' : ' + str(table[key]))
    tree = result
    tac = {'main': []}
    j = 0
    if_count = 0
    global_obhod_for_tac(tree)
    print('__________TAC__________')
    for key in tac:
        print(key + ' : ')
        for i in tac[key]:
            print('\t' + str(i))
    temp_real_tab = {}
    asm(tac, table)



