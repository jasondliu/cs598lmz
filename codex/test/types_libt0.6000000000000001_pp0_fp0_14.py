import types
types.ClassType
types.FunctionType
types.TypeType

# object types
type(int)
type(str)
type(int) == type(str)
type(int) == type
type(int) == types.TypeType

# instance types
type(1)
type('a')
type(1) == type('a')
type(1) == type(int)
type(1) == type(str)
type(1) == type(type(1))

# builtin types
type([1, 2, 3])
type((1, 2, 3))
type({'a': 1, 'b': 2})
type(set([1, 2, 3]))
type(frozenset([1, 2, 3]))
type(slice(1, 2, 3))
type(xrange(1))
type(Ellipsis)
type(None)

# file types
type(open('/etc/passwd'))

# custom types
class MyClass(object):
    def __init__(self, value):
        self.value = value

   
