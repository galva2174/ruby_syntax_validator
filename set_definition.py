from ply import lex, yacc

# Lexer

tokens = (
    'IDENTIFIER',
    'EQUALS',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'COLON',
    'STRING',
    'NUMBER',
)

t_EQUALS = r'='
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_COLON = r':'

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'IDENTIFIER'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser

def p_set_dict_assignment(p):
    '''
    set_dict_assignment : IDENTIFIER EQUALS set
                       | IDENTIFIER EQUALS dictionary
    '''
    p[0] = {'name': p[1], 'type': p[3]['type'], 'value': p[3]}

def p_set(p):
    'set : LBRACE elements RBRACE'
    p[0] = {'type': 'set', 'elements': p[2]}

def p_dictionary(p):
    'dictionary : LBRACE key_value_pairs RBRACE'
    p[0] = {'type': 'dictionary', 'key_value_pairs': p[2]}

def p_elements(p):
    '''
    elements : elements COMMA element
             | element
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_element(p):
    '''
    element : NUMBER
            | STRING
    '''
    p[0] = p[1]

def p_key_value_pairs(p):
    '''
    key_value_pairs : key_value_pairs COMMA key_value_pair
                   | key_value_pair
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_key_value_pair(p):
    'key_value_pair : IDENTIFIER COLON element'
    p[0] = {'key': p[1], 'value': p[3]}

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

# Example usage

while True:
    try:
        s = input('Enter set/dictionary assignment syntax: ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(f'Syntax Validated: {result}')
