import types
types.MethodType(method, obj)

#利用types模块实现类的动态创建
import types
def fn(self, name='world'):
    print('hello %s' % name)

Hello = type('Hello', (object,), dict(hello=fn))   #创建Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

#metaclass
#先定义metaclass，就可以创建类，最后创建实例

#metaclass是类的模板，所以必须从`type`类型派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)

