import ply.lex as lex
import ply.yacc as yacc

# Lexer

tokens = (
    'IDENTIFIER',
    'LPAREN',
    'RPAREN',
    'COLON',
    'NEWLINE',
    'DEF',
    'END',
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_NEWLINE = r'\n+'
t_DEF = r'def'
t_END = r'end'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Check for reserved words
    t.type = 'DEF' if t.value == 'def' else 'END' if t.value == 'end' else 'IDENTIFIER'
    return t

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Parser

def p_function_definition(p):
    '''
    function_definition : DEF IDENTIFIER LPAREN RPAREN COLON NEWLINE function_body END NEWLINE
                       | DEF IDENTIFIER LPAREN RPAREN NEWLINE function_body END NEWLINE
    '''
    print("Valid Ruby function definition")

def p_function_body(p):
    '''
    function_body : NEWLINE
    '''
    pass



parser = yacc.yacc()

# Test the parser
ruby_code = """
def greet():

end"""

lexer.input(ruby_code)
for token in lexer:
    print(token)

parser.parse(ruby_code)
