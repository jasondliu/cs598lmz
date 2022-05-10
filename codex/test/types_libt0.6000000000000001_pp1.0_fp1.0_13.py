import types
types.FunctionType

def fn():
    pass

type(fn) == types.FunctionType

type(abs) == types.BuiltinFunctionType
type(lambda x: x) == types.LambdaType
type((x for x in range(10))) == types.GeneratorType

#使用isinstance()
isinstance('a', str)

#使用dir()
dir('ABC')
len('ABC')
'ABC'.__len__()

class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
len(dog)

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
hasattr(obj, 'x') #有属性'x'吗？
hasattr(obj, 'y')
setattr(obj, 'y', 19) #设置一个属性'y'
