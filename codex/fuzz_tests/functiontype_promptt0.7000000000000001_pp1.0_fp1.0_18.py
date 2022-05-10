import types
# Test types.FunctionType
def f(): pass
def g(): pass

f.foo = 42

f == f
f == g

f != f
f != g

# Test types.UnboundMethodType
class C:
    def meth(self): pass

m = C.meth

m.foo = 42

m == m
m == C.meth

m != m
m != C.meth

# Test types.MethodType
x = C()
m = x.meth

m.foo = 42

m == m
m == x.meth

m != m
m != x.meth

# Test types.BuiltinFunctionType
def h(x): pass

h == h
h == f

h != h
h != f

# Test types.BuiltinMethodType
h == C.meth

h != C.meth

# Test types.ClassType
class D: pass

D == D
D == C

D != D
D != C

# Test types.InstanceType
x = D()

x ==
