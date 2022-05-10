import types
types.MethodType(inMethod, obj)

# 要定义一个class的方法，除了第一个参数是self外，其他和普通函数一样。
# 要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入
# 静态方法和类方法
# 使用@staticmethod或@classmethod，就可以把对应的方法变成静态方法或类方法。
class Student(object):

    @staticmethod
    def isStudent(obj):
        return isinstance(obj,
