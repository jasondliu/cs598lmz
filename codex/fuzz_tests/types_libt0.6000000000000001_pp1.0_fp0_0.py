import types
types.MethodType(lambda self: None, None, None)
'''

# 实例属性和类属性

# 给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
    def __init__(self, name):
        self.name = name

# 给类绑定属性的方法是通过类变量：
class Teacher(object):
    name = 'Teacher'

# 但是，如果Teacher本来就有name属性，
# 这种方法将无法更改Teacher的name属性：
s = Teacher()
print(s.name)
s
