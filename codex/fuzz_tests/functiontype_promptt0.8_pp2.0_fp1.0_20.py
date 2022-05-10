import types
# Test types.FunctionType

if __name__ == '__main__':
    print(type(abs), type(lambda x: x), types.FunctionType)
    f = abs
    print(f)
    print(type(abs) == types.BuiltinFunctionType)
    print(type(f) == types.FunctionType)
    print(isinstance(f, types.BuiltinFunctionType))
    print(isinstance(f, types.FunctionType))


# 链式调用
# 这个没有觉得什么特别，我没用python。
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


# print(Student('Michael'))
# s = Student('Michael')
# # 这个等价于：print(s.__str__
