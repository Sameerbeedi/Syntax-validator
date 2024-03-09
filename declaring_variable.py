# Declaring variable in C#

from ply import lex, yacc

# Define the tokens
tokens = ('DATATYPE', 'VARIABLE', 'SEMICOLON', 'COMMA')

# Define regular expressions for tokens
t_VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_SEMICOLON = r';'
t_DATATYPE = r'\b(int|float|string|bool|char|double)\b'
t_COMMA = r','

# Define a list to store syntax errors
syntax_errors = []

# Define the lexer
def t_error(t):
    syntax_errors.append(f"Syntax error at line {t.lineno}: Unexpected token '{t.value[0]}'")
    t.lexer.skip(1)

# Add a rule to ignore spaces and tabs
t_ignore = ' \t'

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

# Define the parser
def p_program(p):
    '''program : declarations'''
    pass

def p_declarations(p):
    '''declarations : declaration
                   | declarations declaration'''

def p_declaration(p):
    '''declaration : DATATYPE var_list SEMICOLON'''
    datatype = p[1].lower()
    for var in p[2]:
        if datatype not in {'int', 'float', 'string', 'bool', 'char', 'double'}:
            syntax_errors.append(f"Syntax error at line {p.lineno(1)}: Invalid datatype '{datatype}'")
        if not var.isidentifier():
            syntax_errors.append(f"Syntax error at line {p.lineno(2)}: Invalid variable name '{var}'")

def p_var_list(p):
    '''var_list : VARIABLE
                | var_list COMMA VARIABLE'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_error(p):
    if p:
        syntax_errors.append(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")
    else:
        syntax_errors.append("Syntax error at EOF")

parser = yacc.yacc()

# Sample input (with spaces and newlines)
input_text=input("Enter the variable syntax to be validated : ")

# Parse the input
lexer.input(input_text)
for token in lexer:
    pass
parser.parse(input_text)

# Check for syntax errors
if not syntax_errors:
    print("Syntax is valid.")
else:
    print("Syntax errors:")
    for error in syntax_errors:
        print(error)

