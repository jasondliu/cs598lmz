import types
# Test types.FunctionType
def foo():
    pass
#print type(foo)
#print type(foo) == types.FunctionType
#print type(abs) == types.BuiltinFunctionType
#print type(lambda x: x) == types.LambdaType
#print type((x for x in range(10))) == types.GeneratorType

# Test isinstance
#print isinstance([1,2,3], (list, tuple))
#print isinstance((1,2,3), (list, tuple))

# Test dir
#print dir('ABC')
#print len('ABC')
#print 'ABC'.__len__()

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

# Test getattr
obj = MyObject()
#print hasattr(obj, 'x')
#print obj.x
#print hasattr(obj, 'y')
#print setattr(obj, 'y', 19)
#print hasattr(obj, 'y')
#print getattr
