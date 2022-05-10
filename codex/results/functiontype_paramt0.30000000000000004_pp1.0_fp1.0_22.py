from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# class
class A:
    def __init__(self):
        self.a = 1
    def __getitem__(self, item):
        return item
    def __repr__(self):
        return 'A'

list(A())

# generator
list(x for x in range(10))

# generator expression
list(x for x in range(10))

# list
list([1, 2, 3])

# set
list({1, 2, 3})

# tuple
list((1, 2, 3))

# dict
list({'a': 1, 'b': 2})

# range
list(range(10))

# str
list('abc')

# bytes
list(b'abc')

# bytearray
list(bytearray(b'abc'))

# memoryview
list(memoryview(b'abc'))
