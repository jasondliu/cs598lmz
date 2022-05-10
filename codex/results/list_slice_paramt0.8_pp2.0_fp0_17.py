import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

# 对象在一个循环引用中，当某个b对象的弱引用被删除的时候，c对象和d对象都被删除了
import weakref
class A(object):
    def __init__(self,name):
        self.nam=name
    def __repr__(self):
        return 'A(%s)'%(self.nam)
a=A('a')
b=A('b')
c=A('c')
d=A('d')
a.c=c
c.d=d
d.b=b
b.a=a
def callback(x):
    print 'callback:',x
keepali0e=[]
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref
