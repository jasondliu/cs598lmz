import types
types.MethodType(func, obj)

# 对于class的绑定类函数和对于对象绑定的函数，它们的区别就是
# 调用方法时会有self参数传递，而对象绑定方法无self参数传递


# class Student(object):
#     __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
# 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 
#     def getName(self):
#         return self.name
# 
#     def getAge(self):
#         return self.age
# 
#     def setAge(
