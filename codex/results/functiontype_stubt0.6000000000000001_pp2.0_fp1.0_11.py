from types import FunctionType
a = (x for x in [1])
b = [1, 2, 3]
c = {1, 2, 3}
d = {1: 2, 3: 4}
e = FunctionType(lambda x: x*x, 1, 2)
f = []
g = {}
h = set()
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h))

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

bart = Student('Bart', 'male')
if bart.gender == 'male':
    print('测试通过!')
else:
    print('测试失败!')

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender


