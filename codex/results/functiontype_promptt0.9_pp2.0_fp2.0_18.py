import types
# Test types.FunctionType

def f():
    pass

x = f()
t1 = type(x)
print(t1)

# Test direct construction of FunctionType, method and call

def f():
    pass


t2 = types.FunctionType( f.__code__, globs={}, name="foo", closure=(f))
print(t2)
print(t2.__name__)

t2 = t2()
print(t2)

# Test direct construction with defaults

def f(x=3):
    pass


t3 = types.FunctionType( f.__code__, globs={}, name="foo", closure=(f))
print(t3)
print(t3.__name__)

t3 = t3()
print(t3)

# Test type of function built directly

t4 = types.FunctionType( f.__code__, globs={}, name="foo", closure=(f))
print(t4)
print(t4.__name__)

t4 = t4()
print(t4)

t
