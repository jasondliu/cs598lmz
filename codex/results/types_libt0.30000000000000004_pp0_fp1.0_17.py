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
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作
