import types
# Test types.FunctionType(function)

def foo():
    pass

def bar():
    pass

f = types.FunctionType(foo, globals(), "foo")

if f != foo:
    print "Error: __new__ returns incorrect function"

try:
    f = types.FunctionType(bar, globals(), "foo")
except TypeError:
    pass # OK
else:
    print "Error: __new__ doesn't raise TypeError on wrong name"

try:
    f = types.FunctionType(bar, globals(), "bar")
except TypeError:
    print "Error: __new__ raises TypeError on correct name"

try:
    f = types.FunctionType(foo, globals())
except TypeError:
    pass # OK
else:
    print "Error: __new__ doesn't raise TypeError on wrong arg count"

# Test types.FunctionType(code, globals, name, argdefs, closure)

def foo(x, y = 2, *z):
    pass

def bar(x, y = 2, *z):
   
