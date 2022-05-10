from types import FunctionType
a = (x for x in [1])
a.__class__

class Foo:


    def func(self):
        print("aaa")

    def __call__(self, *args, **kwargs):
        print("name: ", self.__name__)

f = Foo() # 相当于调用 __new__()创建对象并返回当前实例对象

f.func() # 调用函数,即调用 __call__ 函数

#dir(f)

#type(f.func)

type(Foo.func)



class C():
    def f(self, x):
        return x
    classmethod(f)
    @staticmethod
    def g(x):
        return x


c = C()

#c.g(1)

def call(self, *args, **kwargs):
    print("name: ", self.__name__)

Foo.func =
