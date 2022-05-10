import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
#keepalive=[a]
keepalive=[a,a.c]
ref=weakref.ref(a,callback)
del a
print(len(lst))
keepali0e=[]
print(len(lst))


#可以用__slots__来创建只能存一个实例数据的类
class Singleton_0(object):
    _state={}
    def __new__(cls, *args, **kwargs):
        ob=super(Singleton_0,cls).__new__(cls,*args,**kwargs)
        ob.__dict__=cls._state
        return ob
class Singleton_1(object):
    _state={}
    def __new__(cls, *args, **kwargs):
        ob=super(Singleton_1,cls).__new__(cls,*args,**kwargs)
        ob.__dict__=cls._state
        return ob

