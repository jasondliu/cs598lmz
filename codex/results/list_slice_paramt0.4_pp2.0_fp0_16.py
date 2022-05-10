import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst

#weakref.ref()的回调函数
import weakref
class A(object):pass
def callback(x):
    print('callback',x)
a=A()
r=weakref.ref(a,callback)
r
r()
del a

#weakref.WeakKeyDictionary()
import weakref
class A(object):pass
a=A()
d=weakref.WeakKeyDictionary()
d[a]='hello'
d
d[a]
del a
d

#weakref.WeakValueDictionary()
import weakref
class A(object):pass
a=A()
d=weakref.WeakValueDictionary()
d[1]=a
d
d[1]
del a
d

#weakref.WeakSet()
import weakref
class A(object):pass
a=A()
s=weakref.WeakSet()
s.add(a)
s
s.add(a)
s
del a
s
