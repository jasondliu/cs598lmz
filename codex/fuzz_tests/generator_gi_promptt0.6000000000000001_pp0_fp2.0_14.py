gi = (i for i in ())
# Test gi.gi_code.co_freevars

def f(x):
    def g(y):
        return x + y
    return g

g = f(1)
print(g(2))
print(g.__closure__[0].cell_contents)
print(g.__code__.co_freevars)

# Test gi.gi_frame.f_locals

def f():
    x = 1
    y = 2
    return locals()

print(f())

# Test gi.gi_frame.f_globals

def f():
    return globals()

print(f()['f'])

# Test gi.gi_frame.f_code

def f():
    return f.__code__

print(f())

# Test gi.gi_frame.f_trace

def f():
    return sys._getframe(0).f_trace

print(f())

# Test gi.gi_frame.f_lasti

def f():
    return sys._getframe(0).
