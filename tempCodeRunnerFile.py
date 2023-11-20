import ply.lex as lex
import ply.yacc as yacc

# Lexer tokens
tokens = (
    'VALUE',
    'COLON',
    'COMMA',
    'LBRACE',
    'RBRACE',
    'VARIABLE',
    'IDENTIFIER',
    'EQUAL'
)

# Lexer rules
t_COLON = r':'
t_COMMA = r','
t_LBRACE = r'{'
t_RBRACE = r'}'
t_EQUAL = r'='

def t_VALUE(t):
    r'".*"'
    return t

t_IDENTIFIER = r'[a-zA-Z_"][a-zA-Z0-9_"]*'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Parser rules
def p_hash(p):
    '''hash : IDENTIFIER EQUAL LBRACE key_value_pairs RBRACE'''
    p[0] = {p[2]: dict(p[3])}

def p_key_value_pairs(p):
    '''key_value_pairs : key_value_pairs COMMA key_value_pair
                      | key_value_pair
                      | empty'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_key_value_pair(p):
    '''key_value_pair : IDENTIFIER COLON VALUE
                        | empty'''
    p[0] = (p[1], p[3])
def p_empty(p):
    '''
    empty :
    '''

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Test input strings

input_string2 = 'my_hash = { key1: "value1", key2: "value2", key3: "value3" }'

# Test the lexer and parser
lexer.input(input_string2)
for token in lexer:
    print(token)

result = parser.parse(input_string2, lexer=lexer)
print(result)
