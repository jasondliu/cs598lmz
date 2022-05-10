import types
# Test types.FunctionType
def f1():
    pass
def f2(x, y):
    return x + y
def f3(*args):
    return args
def f4(**kwargs):
    return kwargs
def f5(x):
    x[0] += 1
def f6(x):
    x += 1
print type(f1)
print type(f2)
print type(f3)
print type(f4)
print type(f5)
print type(f6)

# Test types.GeneratorType
def gen():
    yield 1
print type(gen())

# Test types.TracebackType
try:
    raise Exception('test')
except:
    tb = sys.exc_info()[2]
print type(tb)

# Test type.TypeType
print type(type)

# Test types.XRangeType
print type(xrange(1))

# Test types.UnboundMethodType
class A(object):
    def f(self):
        pass
print type(A.f)

# Test
