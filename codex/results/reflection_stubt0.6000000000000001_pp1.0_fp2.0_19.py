fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# 使用反射修改对象的类型
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self):
        print("dog init")

a = Animal("a")
print(a.name)
a.__class__ = Dog
a.__init__() # 注意此时调用的是Dog的init方法

# 参考：https://www.zhihu.com/question/288972434/answer/639040599
