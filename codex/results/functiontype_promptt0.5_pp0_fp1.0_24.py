import types
# Test types.FunctionType
def add(a,b):
    return a + b
print(type(add))
print(type(abs))
print(type(lambda x:x))
print(type(x for x in range(10)))
print(type(100))

# Test types.MethodType
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
# getattr(obj, 'z')
print(getattr(obj, 'z', 404))

# Test types.BuiltinMethodType
print(len)
print(hasattr(len, '__call__'))

# Test types.LambdaType
print(type(lambda x:
