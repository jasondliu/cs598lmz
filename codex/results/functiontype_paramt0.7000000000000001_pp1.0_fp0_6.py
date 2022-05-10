from types import FunctionType
list(FunctionType(lambda: 1).__dict__.items())
# [('__func__', <function <lambda> at 0x7f444424d158>)]

import inspect

def f():
    pass

def g():
    pass

print(inspect.isfunction(f))
print(inspect.isfunction(g))
print(inspect.isfunction(g.__code__))
print(inspect.isfunction(inspect.isfunction))

# True
# True
# False
# True

print(inspect.isroutine(f))
print(inspect.isroutine(g))
print(inspect.isroutine(g.__code__))
print(inspect.isroutine(inspect.isfunction))


# True
# True
# True
# True

print(inspect.isclass(f) )
print(inspect.isclass(g) )
print(inspect.isclass(g.__code__) )
print(inspect.isclass(inspect.isfunction) )

# False
# False
