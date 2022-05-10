from types import FunctionType
list(FunctionType(lambda:None,{}).__code__.co_consts)

# [None, '<lambda>', '<listcomp>', '<dictcomp>']

# The code object of a function is immutable.
# The code object of a function is shared by all instances of the same function.

# The code object of a function is a read-only attribute.
# However, the code object of a function can be replaced with another code object.
# This is the basis of the Python bytecode disassembler module, dis.

# The code object of a function is a read-only attribute.
# However, the code object of a function can be replaced with another code object.
# This is the basis of the Python bytecode disassembler module, dis.

# The code object of a function is a read-only attribute.
# However, the code object of a function can be replaced with another code object.
# This is the basis of the Python bytecode disassembler module, dis.

# The code object of a function is a read-only attribute.
# However, the code object of a function can be replaced with
