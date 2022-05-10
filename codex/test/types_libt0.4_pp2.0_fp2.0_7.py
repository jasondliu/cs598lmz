import types
types.MethodType(lambda self: '', None, None)

# Test that we can get a function's code object
def f(): pass
f.func_code

# Test that we can get a function's globals
def g(): pass
g.func_globals

# Test that we can get a function's dict
def h(): pass
h.__dict__

# Test that we can get a function's default arguments
def i(a, b=1): pass
i.func_defaults

# Test that we can get a function's closure
def j():
    a = 1
    def k():
        return a
    return k
l = j()
l.func_closure

# Test that we can get a function's doc string
def m(): pass
m.__doc__

# Test that we can get a function's name
def n(): pass
n.__name__

# Test that we can get a function's module
def o(): pass
o.__module__

# Test that we can get a function's dict
def p(): pass
p.__dict__
