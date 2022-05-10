import types
# Test types.FunctionType
def fn1(a):
    print a

if type(fn1) == types.FunctionType:
    print 'fn1 is function'
else:
    print 'fn1 isn\'t function'

# Test types.MethodType
class A:
    def __init__(self):
        self.a = 'a'
    def fn2(self):
        print self.a

if type(A.fn2) == types.MethodType:
    print 'A.fn2 is method'
else:
    print 'A.fn2 isn\'t method'

# Test types.StringType
if type('A') == types.StringType:
    print 'A is string'
else:
    print 'A isn\'t string'

# Test types.TypeType
if type(A) == types.TypeType:
    print 'A is type'
else:
    print 'A isn\'t type'

# Test types.LambdaType
fn3 = lambda x: x*x
if type(fn3) == types.LambdaType:
    print
