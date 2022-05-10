import types
types.MethodType(f,None,Student)

# __slots__
# 只允许对Student实例添加name和age属性
class Student(object):
    __slots__ = ('name', 'age')

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# ERROR: AttributeError: 'Student' object has no attribute 'score'
