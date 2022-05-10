import types
types.ClassType

# 类变量

# 类本身
class Language(object):
    languages = []
    def __init__(self, name):
        self.name = name
        self.languages.append(self)

a = Language('a')
b = Language('b')
print('a.languages', a.languages)
print('Language.languages', Language.languages)

# 类变量引用
class Person(object):
    words = []

    def __init__(self, name):
        self.name=name
        self.words.append(self)

a = Person('a')
b = Person('b')
c = Person('c')
print(a.words)
print(Person.words)

# 实例变量
class A(object):
    a = 1

a = A()
b = A()

