from types import FunctionType
a = (x for x in [1])
b = [1]
print(type(a))
print(type(b))
print(type(FunctionType))
print(type(int))

class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self,attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda : 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

# 测试:
s = Student()
print(s.name)
print(s.score)
print(s.age())
#print(s.abc)

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().
