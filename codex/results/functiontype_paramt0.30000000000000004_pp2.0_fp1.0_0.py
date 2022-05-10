from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 利用属性描述符来实现单例模式
class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}
    def __call__(self, *args, **kwargs):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls(*args, **kwargs)
        return self._instance[self._cls]

@Singleton
class A(object):
    def __init__(self, x=0):
        self.x = x

a1 = A(2)
a2 = A(3)
a1 is a2

# 利用元类来实现单例模式
class SingletonType(type):
    def __init__(self, *args, **kw
