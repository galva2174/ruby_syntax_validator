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
    print(f"Valid syntax: {p[1]}")

def p_key_value_pairs(p):
    '''key_value_pairs : key_value_pairs COMMA key_value_pair
                      | key_value_pair
                      | empty'''

def p_key_value_pair(p):
    '''key_value_pair : IDENTIFIER COLON VALUE
                        | empty'''

def p_empty(p):
    '''
    empty :
    '''

def p_error(p):
    raise SyntaxError(f"Invalid syntax at line {p.lineno}, position {p.lexpos}, token {p.type}: {p.value}")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Test input string
input_string = 'my_hash =  key1: "value1", key2: "value2" key3: "value3" }'

# Test the lexer and parser
lexer.input(input_string)
for token in lexer: 
    print(token)

try:
    parser.parse(input_string, lexer=lexer)
    print("Parsing successful")
except SyntaxError as e:
    print(e)
