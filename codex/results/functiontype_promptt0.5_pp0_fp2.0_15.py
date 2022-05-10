import types
# Test types.FunctionType()

def func1():
    pass

print(type(func1))

print(type(abs))

print(type(lambda x:x))

print(type((x for x in range(10))))

print(type(x for x in range(10)))

print(type(int))

def fn(self,name='world'):
    print('hello,%s' % name)

Hello = type('Hello',(object,),dict(hello=fn))
h = Hello()
h.hello()

print(type(Hello))

print(type(h))

#metaclass
# 先定义metaclass，就可以创建类，最后创建实例
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(
