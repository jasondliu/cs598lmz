fn = lambda: None
# Test fn.__code__
try: fn.__code__.co_filename
except AttributeError: print >>sys.stderr, "pypy: no fn.__code__"
# Test conditional exprs
x = 3 <= 4 and "foo" or "bar"
# Test if-by-ref codegen
def try_del_finally():
    y = 10
    try:
        y += 10
    finally:
        y -= 1
try_del_finally()
# Test int() constructor
z = int(12)
w = int()
if str(z) != "12": raise ValueError
# Test delattr()
class A:
    def __delattr__(self, name):
        print "delattr", name
a = A()
del a.foo
# Test kwargs
def kwarg(**kwargs):
    for key, value in kwargs.items():
        print key, value
kwarg(a=12, b=13, d=15)
# Test varargs
def vararg(*args):
    for arg in args:
        print arg
var
