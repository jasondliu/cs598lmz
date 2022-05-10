from types import FunctionType
list(FunctionType(tree.body[0], {}).__code__.co_consts)

# CPython's internal representation of a function's code object.
FunctionType(tree.body[0], {}).__code__

# Extracting the constants
FunctionType(tree.body[0], {}).__code__.co_consts

# Extracting the function's name.
FunctionType(tree.body[0], {}).__code__.co_name

# Extracting the function's arguments.
FunctionType(tree.body[0], {}).__code__.co_varnames

# The bytecode instructions
FunctionType(tree.body[0], {}).__code__.co_code

# The bytecode arguments
dis.dis(FunctionType(tree.body[0], {}).__code__.co_code)

# Bytecode arguments
dis.dis(FunctionType(tree.body[0], {}).__code__.co_code)



# Bytecode arguments
dis.dis(FunctionType(tree.body[0], {}).__code__.co_code)


#
