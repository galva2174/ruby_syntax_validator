import ply.lex as lex
import ply.yacc as yacc

# Token definitions
tokens = ('DEF', 'ID', 'LPAREN', 'RPAREN', 'END')

def t_DEF(t):
    r'def'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_LPAREN(t):
    r'\('
    return t

def t_RPAREN(t):
    r'\)'
    return t

def t_END(t):
    r'end'
    return t

t_ignore = ' \t\n'

# Parsing rules
def p_function_definition(p):
    'function_definition : DEF ID LPAREN RPAREN function_body END'
    print("Function definition:", p[2])

def p_function_body(p):
    'function_body : statements'
    pass

def p_statements(p):
    '''statements : statement
                  | statement statements'''

def p_statement(p):
    '''statement : ID
                 | function_definition'''

# Error rule
def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Function to validate syntax
def validate_function_syntax(input_code):
    lexer.input(input_code)
    for tok in lexer:
        print(tok)

    parser.parse(input_code)

# Example usage
input_code = "def my_function() end"
validate_function_syntax(input_code)
