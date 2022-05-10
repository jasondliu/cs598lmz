from types import FunctionType
list(FunctionType(print.__code__, globals(), 'print'))

# The same applies to generaors.
def echoes(start, end):
    for i in range(start, end):
        yield i

print(next(echoes(3, 8)))
a = echoes
echoes(4, 9)

type(echoes)
echoes.__class__
type(echoes) is type(type(echoes))
# They are not the same.
echoes is type(echoes)

a = echoes
a(10, 14)

a = (1, 2, 3)
a = {'a': 1, 'b': 2}
# They create a new namespace proxy.

import sys
print(sys.version)
# sys itself is a module type
type(sys)
# class is a class type.
class Foo:
    pass

# types.ModuleType and class.__class__ both retunr class types.
type(types.ModuleType)
types.ModuleType.__class__ == class.__class__
import types
# It is not the instance
