import types
types.ClassType

# 判断一个对象是否是函数
def fn():
    pass

type(fn) == types.FunctionType
type(abs) == types.BuiltinFunctionType
type(lambda x: x) == types.LambdaType
type((x for x in range(10))) == types.GeneratorType

# 使用isinstance()
isinstance([1, 2, 3], (list, tuple))
isinstance((1, 2, 3), (list, tuple))

# 使用dir()
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
