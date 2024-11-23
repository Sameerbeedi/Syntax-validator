 # Python Syntax Validation using Lex and Yacc
## Project Overview
- This project validates the syntax of Python files using Lex (for lexical analysis) and Yacc (for parsing and syntax validation). 
- It checks whether the provided Python scripts adhere to basic syntax rules for constructs such as variable declarations, function definitions, and control structures<br>
 ### Requirements
- Python 3.x
- PLY library
### Install it via pip:
`pip install ply`
## How to Use
- Place Python Files to Validate
- Add your Python files (e.g., array_declaration.py, declaring_variable.py, etc.) in the project directory.

- Run the Main Script
- Use the main.py script to validate the files:<br>
  `python main.py`
- The script will tokenize and parse each file.
- It will indicate if the syntax is valid or report any errors with line numbers and details.
## Features
- Lexical Analysis: Tokenizes Python constructs such as keywords, identifiers, operators, and literals.
- Parsing: Validates syntax for:
- Variable declarations
- Function definitions
- Control structures (if, else, etc.)
- Error Reporting: Provides detailed error messages with line numbers.
## Limitations
- This implementation only validates syntax, not runtime logic.
- Limited to basic Python constructs defined in the lexer and parser.
