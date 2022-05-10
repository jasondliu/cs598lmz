from types import FunctionType
list(FunctionType(lambda x:x, globals(), 'lambda'))

# To get the source code of a function, use the __code__ attribute.
def add(x, y):
    return x + y

add.__code__
add.__code__.co_code

# The dis module can be used to disassemble the function's bytecode.
import dis
dis.dis(add)

# The bytecode is a sequence of instructions that the interpreter executes.
# Each instruction is a single byte, with the high-order bits used to indicate
# the operation, and the low-order bits used to encode the arguments to the
# operation.

# The first byte of the bytecode is the opcode LOAD_FAST, with argument 0.
# This loads the argument named x from the local namespace.
# The next byte is LOAD_FAST with argument 1, which loads the argument named y.
# The next two bytes are the opcode for the BINARY_ADD operation.
# The final byte is the opcode for the RETURN_VALUE operation.

# The argument to BINARY_ADD is a
