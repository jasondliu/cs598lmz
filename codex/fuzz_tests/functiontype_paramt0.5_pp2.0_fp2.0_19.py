from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'f'))

# __name__
FunctionType(lambda x: x, globals(), 'f').__name__

# __defaults__
def f(a, b=2):
    pass
f.__defaults__

# __code__
FunctionType(lambda x: x, globals(), 'f').__code__

# __globals__
FunctionType(lambda x: x, globals(), 'f').__globals__

# __dict__
def f():
    """doc"""
f.__dict__

# __closure__
def make_adder(n):
    def adder(x):
        return x + n
    return adder

adder = make_adder(2)
adder(1)

# __annotations__
def f(a: 'annotation'):
    pass

f.__annotations__

# __kwdefaults__
def f(a, b=2, *, c=3, d=4):
    pass

f.__kwdefaults__


