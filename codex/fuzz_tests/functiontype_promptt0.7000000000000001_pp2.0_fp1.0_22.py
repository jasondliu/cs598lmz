import types
# Test types.FunctionType
def f():
   pass
print(type(f)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

# Use isinstance()
print(isinstance(f,types.FunctionType))

# Use dir()
print(dir('ABC'))

# Set attr
class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x
obj=MyObject()

# hasattr()
print(hasattr(obj,'x'))
print(obj.x)
print(hasattr(obj,'y'))
setattr(obj,'y',19)
print(hasattr(obj,'y'))
print(getattr(obj,'y'))

# getattr()
print(getattr(obj,'z',404))

# getattr()
f=getattr
