from types import FunctionType
a = (x for x in [1])
print(isinstance(a,FunctionType))

class Foo():
    pass
print(isinstance(Foo,FunctionType))


import types
print(dir(types))

import types
def fn():
    pass

print(types.FunctionType == type(fn))

def fn2():
    pass

def fn3():
    pass

def fn1():
    yield fn2()
    yield from fn3()

print(type(fn1()))
print(type(fn1))

#--------------------------------------------------------------------------------------

def foo(param1,param2):
    res = param1 + param2
    print("%s + %s = %s" % (param1, param2, res))
    return res

fn = foo
print(foo)
print(fn)

x = foo(1, 2)
print(x)
y = fn(3, 4)
print(y)

print(fn(2, 3))


#--------------------------------------------------------------------------------------

import types

def foo():
    pass

print(type(foo) ==
