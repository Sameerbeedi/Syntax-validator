# Function declaration for C#
import ply.lex as lex
import ply.yacc as yacc

# Define the tokens
tokens = ('AMODIFIER', 'RTYPE', 'NAME', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON', 'COMMA', 'COMMENT', 'ASSIGN', 'PRINT', 'RETURN', 'NUMBER')

t_AMODIFIER = r'(public|private|protected|internal)'
t_RTYPE = r'\b(void|int|float|char|string)\b'
t_NAME = r'(?!return\b|print\b|public\b|private\b|protected\b|internal\b|void\b|int\b|float\b|char\b|string\b)([a-zA-Z_][a-zA-Z0-9_]*)\b'
t_COMMENT = r'//.*'
t_ASSIGN = r'='
t_SEMICOLON = r';'
t_COMMA = r','
t_PRINT = r'print'
t_RETURN = r'return'
t_NUMBER = r'\d+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

# Define a list to store syntax errors
syntax_errors = []

# Define the lexer
def t_error(t):
    syntax_errors.append(f"Syntax error at line {t.lineno}: Unexpected token '{t.value}'")
    t.lexer.skip(1)

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
    '''declaration : AMODIFIER RTYPE NAME LPAREN parameter_list RPAREN LBRACE statements RBRACE'''

def p_parameter_list(p):
    '''parameter_list : parameter
                     | parameter_list COMMA parameter'''

def p_parameter(p):
    '''parameter : RTYPE NAME'''

def p_statements(p):
    '''statements : statement
                  | statements statement'''

def p_statement(p):
    '''statement : other_statement
                 | SEMICOLON
                 | comment
                 | assignment
                 | function_call
                 '''

def p_comment(p):
    '''comment : COMMENT'''

def p_assignment(p):
    '''assignment : RTYPE NAME ASSIGN expression SEMICOLON'''

def p_function_call(p):
    '''function_call : NAME LPAREN argument_list RPAREN SEMICOLON'''

def p_other_statement(p):
    '''other_statement : RETURN expression SEMICOLON
                        | PRINT expression SEMICOLON '''

def p_argument_list(p):
    '''argument_list : arguments
                    | empty'''

def p_arguments(p):
    '''arguments : argument
                | arguments COMMA argument'''

def p_argument(p):
    '''argument : expression'''

def p_expression(p):
    '''expression : LPAREN expression RPAREN
                   | NAME 
                   | NUMBER'''

def p_empty(p):
    'empty :'

def p_error(p):
    print(p)
    if p:
        syntax_errors.append(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")
    else:
        syntax_errors.append("Syntax error at EOF")

parser = yacc.yacc()

# Sample input 
print("Enter function declaration code. Type 'end' on a new line to finish:")
print("Use 'end' as the last line to indicate the end of input.")

input_lines = []
while True:
    line = input()
    if line.strip().lower() == 'end':
        break
    input_lines.append(line)

# Combine the lines into a single string
input_text = '\n'.join(input_lines)
# Parse the input
lexer.input(input_text)
for token in lexer:
    print(token)
    pass

parser.parse(input_text)

# Check for syntax errors
if not syntax_errors:
    print("Syntax is valid.")
else:
    print("Syntax errors:")
    for error in syntax_errors:
        print(error)
