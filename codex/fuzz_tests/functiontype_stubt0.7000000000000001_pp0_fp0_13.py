from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print('-'*20)
# ---------- 判断某个类是否有某些属性/方法
class Foo(object):
    def __init__(self, name):
        self._name = name
    def printname(self):
        print(self._name)
f = Foo('qiyue')
hasattr(f, '_name') # 判断是否有这个属性
hasattr(f, 'printname') # 判断是否有这个方法

print('-'*20)
# ---------- 判断某个对象是否有某个属性/方法
class Foo(object):
    def __init__(self, name):
        self._name = name
    def printname(self):
        print(
