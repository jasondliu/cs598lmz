from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# [Out]: ['<lambda>']

# The code object is a read-only object that contains the bytecode that
# implements the function body.
#
# The co_varnames attribute is a tuple containing the names of the local
# variables (including arguments).
#
# The co_argcount attribute is the number of arguments (including arguments
# with default values).

# The co_code attribute is a bytes object containing the sequence of bytecode
# instructions.

# The dis module can be used to disassemble the bytecode.

from dis import dis

dis(lambda: None)

# [Out]:
#   2           0 LOAD_CONST               0 (None)
#               2 RETURN_VALUE

# The bytecode is a sequence of instructions, each one represented by a single
# byte.
#
# The first byte of the sequence is an opcode identifying the instruction.
#
# The remaining bytes are arguments for the instruction.
#
# The dis module shows the instruction and its arguments in a human
