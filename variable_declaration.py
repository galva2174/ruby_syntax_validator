from ply import lex, yacc

# Lexer
tokens = (
    'IDENTIFIER',
    'EQUALS',
    'STRING',
    'NUMBER',
    'BOOLEAN',
)

t_EQUALS = r'='
t_STRING = r'"[^"]*"'
t_BOOLEAN = r'true|false'
t_ignore = ' \t\n'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser
def p_statement_assignment(p):
    'statement : IDENTIFIER EQUALS value'
    print("Valid Syntax")

def p_value(p):
    '''value : STRING
             | NUMBER
             | BOOLEAN
             | IDENTIFIER'''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {find_column(p.lexer.lexdata, p)}: Unexpected token '{p.value}'")
    else:
        print("Syntax error: unexpected end of input")

def find_column(lexer_input, token):
    last_cr = lexer_input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

parser = yacc.yacc()

# Test the parser
code = input("Enter code:")
lexer.input(code)
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)

parser.parse(code)
