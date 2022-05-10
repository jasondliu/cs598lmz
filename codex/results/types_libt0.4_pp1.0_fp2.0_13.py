import types
types.MethodType(func, obj)

# 使用__slots__
# 在Python中，每个类都有实例属性。通常，在__init__方法中，我们都会用self.xxx来定义实例属性。比如下面的Student类：
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到
