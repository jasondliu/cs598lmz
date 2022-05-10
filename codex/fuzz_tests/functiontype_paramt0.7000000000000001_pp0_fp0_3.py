from types import FunctionType
list(FunctionType(code_obj,globals(),'foo'))

# 如果一个类定义了__call__方法，它就可以像函数那样被调用
class A:
    def __init__(self,x):
        self.x = x
    def __call__(self,y):
        return self.x * y
a = A(5)
a(10)
a.__call__(10)

# 可调用对象
# 函数对象和类是可调用对象，函数是绑定的可调用对象，类是未绑定的可调用对象
# 调用一个类的实例，
