from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(FunctionType))
print(isinstance(a,FunctionType))
print(callable(a))

# 类的实例都有__call__方法，可以直接对实例进行调用
class A:
    def __init__(self,name):
        self.name = name
    def __call__(self, *args, **kwargs):
        print('My name is %s' % self.name)
a = A('Alex')
a()

# 可调用对象还可以用做装饰器
def dec(func):
    def in_dec(*args):
        print('in dec arg =',args)
        if len(args)==0:
            return 0
        for val in args:
            if not isinstance(val,int):
                return 0
        return func(*args)
    return in_
