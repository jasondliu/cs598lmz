import types
# Test types.FunctionType
def function(x):
    print x

if type(function) is types.FunctionType: print "yes"

# Test types.LambdaType
x = lambda: None
if type(x) is types.LambdaType: print "yes"

# Test types.GeneratorType
x = (i for i in range(0))
if type(x) is types.GeneratorType: print "yes"

# Test unsupported numeric types
import sys
if sys.version < '2.5':
    class foo: pass
    class C(float):
        pass
    class D(int):
        pass
    class E(long):
        pass

    instance_C = C()
    instance_D = D()
    instance_E = E()

    for t in (foo, C, D, E):
        try:
            eval('class %s2(%s, int): pass' % (t.__name__, t.__name__))
        except TypeError, detail:
            print detail
        try:
            eval('class %s3(int,
