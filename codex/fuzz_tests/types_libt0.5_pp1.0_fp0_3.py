import types
types.FunctionType

class A(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        self.c = 'c'
        self.d = 'd'
        self.e = 'e'

    def __getitem__(self, item):
        return self.__dict__.get(item, None)

a = A()
a['a']

# 反射

class B(object):
    def __init__(self):
        self.a = 'a'

    def __getattr__(self, item):
        return self.__dict__.get(item, None)

b = B()
b.a

# 用于模拟私有属性
class C(object):
    def __getattr__(self, item):
        return self.__dict__.get('_' + item, None)

    def __setattr__(self, key, value):
        self.__dict__['_'
