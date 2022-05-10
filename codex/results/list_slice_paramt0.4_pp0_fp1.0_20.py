import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:
    print(lst)
    time.sleep(0.1)

#模块
import sys
print(sys.modules)
print(sys.modules['sys'])

#元类
class Meta(type):
    def __new__(cls,name,bases,attrs):
        print(cls,name,bases,attrs)
        return type.__new__(cls,name,bases,attrs)
class A(metaclass=Meta):
    pass

#装饰器
def decorator(func):
    def wrapper(*args,**kwargs):
        print('decorator')
        return func(*args,**kwargs)
    return wrapper
@decorator
def func():
    print('func')
func()

#属性
class A(object):
    def __init__(self):
        self.a=1
        self.b=2
    @property
    def c(self):
