import types
# Test types.FunctionType

def f(): pass

class C:
    def m(self): pass

print types.FunctionType, type(f)
print types.MethodType, type(C.m)

try:
    types.FunctionType(1)
except:
    print 'FunctionType(1)'

try:
    types.FunctionType(f, 1)
except:
    print 'FunctionType(f, 1)'

try:
    types.FunctionType(f, globals(), 1)
except:
    print 'FunctionType(f, globals(), 1)'

try:
    types.FunctionType(f, globals())
except:
    print 'FunctionType(f, globals())'

try:
    types.FunctionType(f, globals(), 'f')
except:
    print 'FunctionType(f, globals(), "f")'

try:
    types.MethodType(1, None)
except:
    print 'MethodType(1, None)'

try:
    types.MethodType(f, None)
except:
    print 'Method
