import types
# Test types.FunctionType for function objects
assert type(len) is types.FunctionType
assert type(f) is types.FunctionType
# Test types.LambdaType for lambda objects
assert type(lambda : None) is types.LambdaType
# Test types.CodeType for code objects
assert type(len.__code__) is types.CodeType
assert type(eval("len").__code__) is types.CodeType
assert type((lambda : None).__code__) is types.CodeType
# Test types.MethodType for method objects
class C(object):
    pass
c = C()
def f(self): pass
c.method = types.MethodType(f, c)
assert type(c.method) is types.MethodType
# ensure classes are of type types.ClassType
assert type(C) is types.ClassType
assert type(c) is types.InstanceType
# ensure instance of user class has a User class type
assert type(c) is C
# Test types.UnboundMethodType for method objects
class C(object):
    pass
c = C()
def f(self): pass
