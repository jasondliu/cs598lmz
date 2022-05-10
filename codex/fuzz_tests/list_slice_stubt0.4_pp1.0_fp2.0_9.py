import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)
import weakref
class A(object):
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'A(%s)'%self.name
def callback(x):
    print('callback:',x)
a=A('a')
r=weakref.ref(a,callback)
print(r)
del a
print(r)
import weakref
class A(object):pass
a=A()
b=A()
a.b=b
b.a=a
def callback(x):print(x)
r=weakref.ref(a,callback)
del a
print(r)
print(b.a)
print(b.a.b)
import weakref
class A(object):pass
a=A()
b=A()
a.b=b
b.a=a
def callback(
