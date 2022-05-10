import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst=[]
print(a.c)

import weakref
class C(object):pass
def callback(x):print('callback')
c=C()
c.c=c
w=weakref.ref(c,callback)
c=None
print(w())
