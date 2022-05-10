import types
# Test types.FunctionType
def f(): pass
def g(func): return func()
l = [f, lambda:None]
map(g,l)

# Verify that we're properly handling __class__ as a special attribute.
def fun(x,y): return x + y
fun.__class__ = "type error"
def run():
    try:
        fun(3,4)
    except TypeError:
        pass

def foo():
    l = []
    l.append(lambda: None)
    return l[0]

map(lambda fn: fn(),
    [foo()] * 5000)

def test(l):
    return l[0]

tup = (3, test)

print tup[1](tup)
