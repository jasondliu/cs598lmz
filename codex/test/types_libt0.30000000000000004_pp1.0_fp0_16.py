import types
types.MethodType(f, None, class_name)

# 实例属性和类属性
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

# 给类绑定属性的方法是通过类变量：
class Student(object):
    name = 'Student'

# 如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属
