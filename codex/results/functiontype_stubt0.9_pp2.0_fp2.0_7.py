from types import FunctionType
a = (x for x in [1])
isinstance(a, GeneratorType)

def a():
    pass
isinstance(a, FunctionType)

class A:
    pass
a = A()
isinstance(a, A)

a = slice(1,3,4)
isinstance(a, slice)

a = 'abcde'
isinstance(a, str)

isinstance(a, bytes)

a = True or False 
isinstance(a, bool)

a = 5
isinstance(a, int)

# isinstance(a, long)

isinstance(a, float)

a = [1,2]
isinstance(a, list)

a = (1,2)
isinstance(a, tuple)

a = {1:2}
isinstance(a, dict)

a = {1,2}
isinstance(a, set)

a = frozenset({1,2})
isinstance(a, frozenset)

a = memoryview(b'abc')
isinstance(a, memoryview)
