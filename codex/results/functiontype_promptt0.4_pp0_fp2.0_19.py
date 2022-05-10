import types
# Test types.FunctionType()
def func():
    pass
print(type(func)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)


# Test isinstance()
print(isinstance('a',str))
print(isinstance(123,int))
print(isinstance(b'a',bytes))

# Test dir()
print(dir('abc'))

# Test len()
print(len('abc'))
print(len(b'abc'))
print(len([1,2,3]))
print(len((1,2,3)))

# Test getattr()
class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x
obj=MyObject()
print(hasattr(obj,'x'))
print(obj.x)
print(hasattr(obj,'y'
