from types import FunctionType
list(FunctionType(lambda: None, {})())
list(FunctionType(lambda: None, {}))
list(FunctionType(lambda: None, {})())
list(FunctionType(lambda: None, {}))

# __dir__
dir(dir)
dir(dir)
dir(dir)
dir(dir)

# __class__
class A:
    pass

A().__class__
A().__class__
A().__class__
A().__class__

# __init__
class A:
    def __init__(self):
        pass

A()
A()
A()
A()

# __new__
class A:
    def __new__(cls):
        return object.__new__(cls)

A()
A()
A()
A()

# __del__
class A:
    pass

a = A()
del a
a = A()
del a
a = A()
del a
a = A()
del a

# __call__
class A:
    def __call__(self):
       
