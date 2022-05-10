import types
# Test types.FunctionType and types.LambdaType
# Test types.BuiltinFunctionType and types.BuiltinMethodType
# Test types.MethodType
# Test types.UnboundMethodType

# Test isinstance
# Test issubclass


# Test special case for __new__

class C(object):
    def __new__(cls, *args):
        return None

def test_new():
    c = C(1,2,3)
    if c is not None:
        raise AssertionError, c

# Test new.instancemethod

def f(): pass
def g(): pass
f2 = new.instancemethod(f,g,C)
# Functions with different names but the same code cannot
# be mapped to the same instance method
f3 = new.instancemethod(f,g,C)
if f2 == f3:
    raise AssertionError, '%s == %s' % (f2, f3)
if f2.__self__ is not None:
    raise AssertionError, '__self__ must be None: %r' % f2
