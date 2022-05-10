from types import FunctionType
list(FunctionType(f.__code__,f.__globals__,name=f.__name__,argdefs=f.__defaults__,closure=f.__closure__))

# >> [1, 2, 3]

# 对于类的方法，可以使用实例的__func__属性
class A:
    def f(self,x,y):
        return x+y

a = A()
a.__func__(a,1,2)
# >> 3
