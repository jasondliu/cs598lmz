import types
types.FunctionType

def test():
    pass

type(test)

isinstance(test, types.FunctionType)

# 能用type()判断的基本类型也可以用isinstance()判断
isinstance([1, 2, 3], (list, tuple))

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

obj = MyObject()

hasattr(obj, 'x')
obj.x
hasattr(obj, 'y')
setattr(obj, 'y', 19)
hasattr(obj, 'y')
getattr(obj, 'y')
obj.y

getattr(obj
