import types
types.MethodType(lambda self: None, None, MyClass)

# 使用__slots__
# 用tuple定义允许绑定的属性名称
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# ERROR: AttributeError: 'Student' object has no attribute 'score'
# s.score = 99

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对
