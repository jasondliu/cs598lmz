import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# -----

# Import local modules
import config, lexer, parser, executor

# -----

# Display usage
if len(sys.argv) != 2:
  print("Usage: " + sys.argv[0] + " <input>")
  sys.exit()

# Read input file
input = open(sys.argv[1], "r").read()

# -----

# Start the interpreter
interpreter = executor.Interpreter(config.DEBUG)

# Initialize the lexer
lexer = lexer.Lexer(input)

# Initialize the parser
parser = parser.Parser(lexer.tokens)

# Execute the program
interpreter.execute(parser.ast)

# -----

# Output results
print("\n")
print("INPUT: " + input)
print("LEXER: " + str(lexer.tokens))
