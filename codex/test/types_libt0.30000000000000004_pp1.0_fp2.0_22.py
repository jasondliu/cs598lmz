import types
types.MethodType(f, None, class_name)

# 实例方法
# 实例方法的第一个参数是self，它指向实例本身，self名字是固定的，不能改变
class Student(object):
    def __init__(self, name):
        self.name = name
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# 静态方法
