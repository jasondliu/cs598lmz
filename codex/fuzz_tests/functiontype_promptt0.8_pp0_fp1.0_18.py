import types
# Test types.FunctionType
try:
    def f(): pass
    types.FunctionType(f.func_code,{},None,None)
except:
    print 'FAILED: should have been able to make a function from another function'

# Test types.MethodType
try:
    class C:
        def f(self): pass
    c = C()
    types.MethodType(C.f.im_func, c, C)
except:
    print 'FAILED: should have been able to make a method from a function'

import new
# Test new.instancemethod
try:
    class C:
        def f(self): pass
    c = C()
    new.instancemethod(C.f.im_func, c, C)
except:
    print 'FAILED: should have been able to make an instance method from a function'
