import types
types.MethodType(func, None, class_name)

# 实例方法
# 实例方法的第一个参数是self，它指向实例本身
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson')
bart.score = 59
bart.print_score()
print(bart)

# 类的访问限制
# 如
