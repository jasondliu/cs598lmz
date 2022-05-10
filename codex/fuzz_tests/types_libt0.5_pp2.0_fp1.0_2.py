import types
types.MethodType(func,None,type(func))
type(func)

# 使用__slots__
# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
# 先定义一个函数，当我们传入其它的参数时，报错
def set_age(self,age):
    self.age=age

# 定义一个类
class Student(object):
    __slots__=('name','age') # 用tuple定
