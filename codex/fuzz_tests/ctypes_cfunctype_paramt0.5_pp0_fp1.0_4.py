import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def f(x):
    return x + 1

cfunc = FUNTYPE(f)

print cfunc(1)
print cfunc(2)
print cfunc(3)

# Now using a lambda function

cfunc = FUNTYPE(lambda x: x + 2)

print cfunc(1)
print cfunc(2)
print cfunc(3)

# Now using a function with a default parameter value

def f(x, y=5):
    return x + y

cfunc = FUNTYPE(f)

print cfunc(1)
print cfunc(2)
print cfunc(3)

# Now using a method

class Foo(object):
    def bar(self, x):
        return x + 3

cfunc = FUNTYPE(Foo().bar)

print cfunc(1)
print cfunc(2)
print cfunc(3)
</code>
The output is:
<code>2
3
4
3
4
5
6
