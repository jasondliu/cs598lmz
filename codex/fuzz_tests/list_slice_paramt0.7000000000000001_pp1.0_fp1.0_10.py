import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
lst[0]="Hi there!"
a.c=a
print(lst[0])

import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
ref=weakref.ref(a,callback)
a=None
print(ref())
print(ref())
