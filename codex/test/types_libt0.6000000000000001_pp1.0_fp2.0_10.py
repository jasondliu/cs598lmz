import types
types.MethodType(g, None, Hello)

class Hello2(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
h2 = Hello2()
h2.hello()
print(type(Hello))
print(type(h2))

# metaclass
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
class MyList(list, metaclass=ListMetaclass):
    pass
L = MyList()
L.add(1)
print(L)

# ORM

