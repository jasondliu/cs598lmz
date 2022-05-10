from types import FunctionType
a = (x for x in [1])
a.__name__

def foo(x,y):
    pass
type(foo)
foo.__name__

def foo():
    pass
foo.__name__

f = lambda x: x * 2
f.__name__
type(f)

a = [1,2]
a.__name__

a = 1
a.__name__

a = 'abc'
a.__name__

a = {'a':1}
a.__name__

a = 1.0
a.__name__

a = 1 + 2j
a.__name__

a = set([1,2])
a.__name__

a = frozenset([1,2])
a.__name__

a = bytes('abc','utf-8')
a.__name__

a = bytearray('abc','utf-8')
a.__name__

a = memoryview(bytes('abc','utf-8'))
a.__name__

a = 1
a.__class__

a
