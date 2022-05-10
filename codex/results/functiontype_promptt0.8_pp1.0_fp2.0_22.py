import types
# Test types.FunctionType and types.MethodType

class Foo:
    
    def __init__(self):
        self.x = 42
        
    def print_x(self):
        print self.x
        
def f1(x, y):
    return x + y
    
f2 = Foo()
f3 = Foo()

print "f1: ", type(f1)
print "f2: ", type(f2)
print "f3: ", type(f3)
print "f2.print_x: ", type(f2.print_x)
print "f2.print_x(): ", type(f2.print_x())
print "Foo.print_x: ", type(Foo.print_x)
print "f2.print_x is Foo.print_x: ", (f2.print_x is Foo.print_x)
print "FunctionType: ", types.FunctionType
print "f1 is FunctionType: ", (type(f1) is FunctionType)
print "f2.print_x is FunctionType: ", (type(f2.
