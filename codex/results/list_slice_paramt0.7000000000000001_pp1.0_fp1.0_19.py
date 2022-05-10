import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(weakref.ref(a,callback))
del a
while lst:print(lst)
lst.append('hi')
del lst
while keepali0e:print(keepali0e)
#print(lst)
#print(keepali0e)

import weakref
class A(object):pass
a=A()
b=A()
a.c=b
b.c=a
lst=[a,b]
print(lst)
del a
del b
print(lst)

def callback(x):del lst[:]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
del a
print(lst)
lst.append('hi')
del lst

def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
del a
print(lst)
