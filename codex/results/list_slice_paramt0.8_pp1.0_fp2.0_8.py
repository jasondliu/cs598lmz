import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
lst[0]='a'
a.c=None
del a
print(len(lst))

def callback(x):print(x)
class A(object):pass
a=A()
a.c=a
keepalive=[weakref.ref(a.c,callback)]
a.c=None
del a
输出：None

#使用__weakref__控制对象的弱引用
class Weak:
    def __init__(self):
    def method(self):pass
w=Weak()
w.method()
w2=w.__weakref__()
w2.method()#报错

class Weak:
    __slots__=['__weakref__']
    def __init__(self):
        self.__weakref__=self
    def method(self):pass
w=Weak()
w2=w.__weakref__()
w2.method()

#使用__weakref__
