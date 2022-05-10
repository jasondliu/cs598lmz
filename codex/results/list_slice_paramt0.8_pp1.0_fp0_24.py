import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a, callback))
del a
if len(lst)!=1:print(1)
if len(lst)<>1:print(2)
if len(lst)>1:print(3)
if len(lst)<1:print(4)
if len(lst)==1:print(5)
