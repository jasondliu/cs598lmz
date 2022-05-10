import types
# Test types.FunctionType
f = lambda x,y: x+y
print type(f)==types.FunctionType
f = min
print type(f)==types.FunctionType

# Test types.ClassType
class Cls(object):
    pass
    
print type(Cls)==types.ClassType

# Test types.BuiltinFunctionType
print type(min)==types.BuiltinFunctionType

# Test types.BuiltinMethodType
print type(list.append)==types.BuiltinMethodType

# Test types.MethodType
class Cls(object):
    def myfunc(self,myparam='hello'):
    # Note that myfunc is defined without self,
    # so it will not be a bound method.
        return myparam
        
i = Cls()
print type(i.myfunc)==types.MethodType
