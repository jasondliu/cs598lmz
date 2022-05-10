from types import FunctionType
list(FunctionType(lambda x: x*x, globals(), 'foo')() for i in range(10))

# 一个简单的类
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

# 这是一个类的实例，它们的类型是type
h = Hello()
print(type(Hello))
print(type(h))

# 元类的定义
def fn(self, name='world'):
    print('Hello, %s.' % name)

# 创建Hello class
Hello = type('Hello', (object,), dict(hello=fn))

# 创建一个实例
h = Hello()
print(h.hello())
print(type(Hello))
print(type(h))

# metaclass是创建类，所以必
