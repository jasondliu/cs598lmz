import types
types.MethodType(func, None, type)

# 我们也可以通过定义一个特殊的__slots__变量来限制该class实例能添加的属性：

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# s.score = 99 # 绑定属性'score'

# 使用__slots__要注意，__slots__定义的属性仅对当
