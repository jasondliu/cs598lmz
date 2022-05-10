from types import FunctionType
list(FunctionType(0,0,0).__code__)

# Code objects are the things returned by the built-in compile function,
# and they are stored in functions.
FunctionType(0,0,0).__code__.co_name

# Code objects are immutable
FunctionType(0,0,0).__code__.co_name = 'foo'

# But they are also objects and can be modified
FunctionType(0,0,0).__code__.co_varnames = ('a','b','c')

# The object has an internal representation that is used by the interpreter
# but it can also be accessed
FunctionType(0,0,0).__code__.co_code

# This is a Python 3.2 thing
FunctionType(0,0,0).__code__.co_lnotab

# It is possible to create code objects from scratch
import types
code = types.CodeType(10, 5, 1, 0, b'\x00\x00\x00', (), (), (), '', '', 0, b'\x00\x00\x00\x
