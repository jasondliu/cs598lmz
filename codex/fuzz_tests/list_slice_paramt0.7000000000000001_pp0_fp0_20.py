import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a,callback))
del a
for i in range(0,2):
    assert len(lst)==1
assert len(lst)==0
import weakref
class A(object):pass
def callback(x):print('callback called')
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
keepali0e
def callback(x):print('callback called')
a=[]
keepali0e=weakref.ref(a,callback)
del a
keepali0e
lst=[str()]
def callback(x):del lst[0]
a=[]
keepali0e=weakref.ref(a,callback)
del a
assert len(lst)==1
import weakref
class A(object):pass
def callback(x):print('callback called')
a=A()
keepali0e=weakref.ref(a,callback)
a.c=a
del a
keepali0e
a=[str
