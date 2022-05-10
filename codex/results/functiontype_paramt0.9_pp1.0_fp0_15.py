from types import FunctionType
list(FunctionType(..., ...))
list(FunctionType(lambda x: x, ...))
list(FunctionType(lambda x: x, (..., ...)))

list(ModuleType(...))

list(PythonSuspension(..., ..., None))

list(None)
list(True)
list(bytearray())
list(bytes())
list(dictionary())
list(float())
list(frozenset())
list(int())
list(range(0))
list(set())
list(str())
list(tuple())


#
# map builtin
#

map()
map(...)
map(lambda x: x, ...)

map(function())
map(FunctionType(..., ...))
map(FunctionType(lambda x: x, ...))
map(FunctionType(lambda x: x, (..., ...)))

map(ModuleType(...))

map(PythonSuspension(..., ..., None))

map(None)
map(True)
map(bytearray())
map(bytes())
map(dictionary())
