import types
types.MethodType(method, obj)

# 使用__slots__
# 定义一个class，它的实例能绑定的属性是固定的
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# s.score = 99 # 绑定属性'score'

# 使用@property
# 把一个getter方法变成属性，只需要加上@property就可以了
# 此时
