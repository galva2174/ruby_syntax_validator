import ply.lex as lex
import ply.yacc as yacc
syntax_correct = True
# Lexer
tokens = [
    'CASE',
    'WHEN',
    'END',
    'IDENTIFIER',
    'COLON',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQ',
    'NEQ',
    'LT',
    'LE',
    'GT',
    'GE',
]


t_IDENTIFIER = r'[a-zA-Z_"][a-zA-Z0-9_"]*'  # Updated regular expression
t_COLON = r':'
t_NUMBER = r'\d+'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='

t_ignore = ' \t\n'

# Special case handling for CASE and END
def t_CASE(t):
    r'case'
    return t

def t_END(t):
    r'end'
    return t
def t_WHEN(t):
    r'when'
    return t

# Parser
def p_switch_statement(p):
    '''
    switch_statement : CASE expression COLON when_clauses END
    '''

def p_when_clauses(p):
    '''
    when_clauses : when_clause when_clauses
                 | empty
    '''

def p_when_clause(p):
    '''
    when_clause : WHEN expression COLON statements
    '''

def p_statements(p):
    '''
    statements : statement statements
               | empty
    '''

def p_statement(p):
    '''
    statement : expression
    '''

def p_expression(p):
    '''
    expression : NUMBER
               | IDENTIFIER
               | expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | LPAREN expression RPAREN
               | expression EQ expression
               | expression NEQ expression
               | expression LT expression
               | expression LE expression
               | expression GT expression
               | expression GE expression
    '''

def p_empty(p):
    '''
    empty :
    '''

def p_error(p):
    global syntax_correct
    syntax_correct = False
    print(f"Syntax error at line {p.lineno}, Unexpected token '{p.value}'")
# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Test the parser with a Ruby switch case statement
ruby_code = """
case x:
  when 1:
    a
  when 2:
    b
end
"""

lexer.input(ruby_code)
for token in lexer:
    print(token)
if syntax_correct:
    print("Syntax is correct.")
else: 
    print("Incorrect syntax")
parser.parse(ruby_code)
