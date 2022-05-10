from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

def f():
    pass
print(type(f))

# 创建一个class对象
def fn(self, name='world'):
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

h = Hello()
print(h.hello())
print(type(Hello))

print(type(abs))
print(type(fn))
print(type(lambda x: x))


# metaclass 可以控制类的创建行为，它就是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self
