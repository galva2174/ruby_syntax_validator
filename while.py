import ply.lex as lex
import ply.yacc as yacc

# Global variable to track syntax correctness
syntax_correct = True

# Lexer
tokens = (
    'ID',
    'NUMBER',
    'STRING',
    'EQUALS',
    'LT',
    'GT',
    'LE',
    'GE',
    'EQ',
    'NEQ',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'WHILE',
    'END'
)

t_EQUALS = r'=='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'='
t_NEQ = r'~='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_SEMICOLON = r';'
t_END = r'end'

t_ignore = ' \t\n'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    keywords = {'while', 'end'}  # Add more keywords as needed
    if t.value in keywords:
        t.type = t.value.upper()  # Use uppercase for token type
    else:
        t.type = 'ID'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    t.value = t.value[1:-1]  # remove quotes
    return t

def t_WHILE(t):
    r'while'
    return t

def t_error(t):
    global syntax_correct
    syntax_correct = False
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Parser
def p_while_loop(p):
    '''while_loop : WHILE LPAREN condition RPAREN statements END'''
    if syntax_correct:
        print("Syntax is correct.")

def p_condition(p):
    '''condition : expression
                 | expression EQ expression
                 | expression NEQ expression
                 | expression LT expression
                 | expression LE expression
                 | expression GT expression
                 | expression GE expression'''
    pass

def p_statements(p):
    '''statements : statements statement
                  | empty'''
    pass

def p_statement(p):
    '''statement : ID EQ expression SEMICOLON
                 | WHILE LPAREN condition RPAREN LBRACE statements RBRACE
                 | SEMICOLON'''
    pass

def p_expression(p):
    '''expression : term
                  | expression PLUS term
                  | expression MINUS term'''
    pass

def p_term(p):
    '''term : factor
            | term TIMES factor
            | term DIVIDE factor'''
    pass

def p_factor(p):
    '''factor : ID
              | NUMBER
              | LPAREN expression RPAREN'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    global syntax_correct
    syntax_correct = False
    print(f"Syntax error at line {p.lineno}, position {find_column(p.lexer.lexdata, p)}: Unexpected token '{p.value}'")

def find_column(lexer_input, token):
    last_cr = lexer_input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

lexer = lex.lex()
parser = yacc.yacc()

# Example input
input_code = """while (x > 0) 
    x = x - 1;
end
"""

lexer.input(input_code)
for token in lexer:
    print(token)
if syntax_correct:
    print("Syntax is correct.")
parser.parse(input_code)


