from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(FunctionType()))
#2.类型的检查
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
#3.判断是否是一个对象
print(hasattr(a, '__next__'))
print(hasattr(a, '__call__'))

a = int(1)
print(a)
#4.元类
#4.1定义元类
def fn(self, name='world'):
    print('hello %s' % name)
Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()
#4.2元类的使用
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(
