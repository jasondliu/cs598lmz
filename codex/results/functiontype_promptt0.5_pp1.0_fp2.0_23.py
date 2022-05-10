import types
# Test types.FunctionType

def f(x):
    return x + 1

print types.FunctionType(f.func_code, {})(1)
# Test types.MethodType

class C:
    def f(self, x):
        return x + 1

print types.MethodType(C.f.im_func, None, C)(C(), 1)
# Test types.ClassType

class C:
    def f(self, x):
        return x + 1

print types.ClassType("C", (), {"f" : C.f.im_func})
# Test types.InstanceType

class C:
    def f(self, x):
        return x + 1

c = C()
print types.InstanceType(c)
# Test types.UnboundMethodType

class C:
    def f(self, x):
        return x + 1

print types.UnboundMethodType(C.f.im_func, C)
# Test types.StringType

print types.StringType("")
# Test types.UnicodeType

print types.Unic
