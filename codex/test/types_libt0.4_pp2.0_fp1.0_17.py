import types
types.ClassType

# 对于class的继承，如果一个类想被外界调用，
# 那么必须把类的名称放在__all__中
__all__ = ['Student']

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

# 可以自由地给一个实例变量绑定属性，
# 比如，给实例bart绑
