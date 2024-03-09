# Array declaration in C#

from ply import lex, yacc

tokens = (
    'TYPE',
    'ID',
    'LBRACKET',
    'RBRACKET',
    'SEMICOLON'
)

t_TYPE = r'\b(int|float|char)\b'
t_ID = r'(?!int\b|float\b|char\b)[a-zA-Z_][a-zA-Z0-9_]*'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'

t_ignore = ' \t'

syntax_errors = []

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    syntax_errors.append(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

def p_declaration(p):
    '''declaration : TYPE LBRACKET RBRACKET ID SEMICOLON'''
    pass

def p_error(p):
    syntax_errors.append("Syntax error in input")

lexer = lex.lex()
parser = yacc.yacc()

sample_input = '''
int[] numbers;
'''

lexer.input(sample_input)

for token in lexer:
    print(token)
    
parser.parse(sample_input)

if not syntax_errors:
    print("Syntax is valid.")
else:
    print("Syntax errors:")
    for error in syntax_errors:
        print(error)
