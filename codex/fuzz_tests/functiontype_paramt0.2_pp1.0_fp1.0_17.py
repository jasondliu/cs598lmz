from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 使用元类
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
L

# 元类的定义
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

# 元类的使用
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

# 元类的定义
def fn(self, name='world'):
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict
