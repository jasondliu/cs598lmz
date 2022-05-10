from types import FunctionType
list(FunctionType(lambda: None, globals()) for i in range(10))

# class
class A:
    def __init__(self):
        self.a = 1
        self.b = 2

list(A() for i in range(10))

# dict
list(dict(a=1, b=2) for i in range(10))

# set
list(set([1, 2, 3]) for i in range(10))

# frozenset
list(frozenset([1, 2, 3]) for i in range(10))

# range
list(range(10) for i in range(10))

# tuple
list(tuple([1, 2, 3]) for i in range(10))

# str
list(str(i) for i in range(10))

# bytes
list(bytes(i) for i in range(10))

# bytearray
list(bytearray(i) for i in range(10))

# memoryview
list(memoryview(bytes(i)) for i in range(10))

