import types
# Test types.FunctionType
def test0(a, b, c=0, d=1, *args): return a+b+c+d
def test1(a, b): return a+b
def test2(a, b, c=0, d=1, *args, **keywords):
    pass
def test3(x): "Doc string"
    return x
print "test0 =", test0
print type(test0) is types.FunctionType
print "test1 =", test1
print type(test1) is types.FunctionType
print "test2 =", test2
print type(test1) is types.FunctionType
print "test3 =", test3
print type(test1) is types.FunctionType

# Test types.UnboundMethodType
class A:
    def __init__(self, a, b, c, d): self.Sum = a+b+c+d
    def Imethod(self, a, b, c=0, d=1, *args): return a+b+c+d
    def Cmethod(cls, a, b, c
