import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
while lst:
 keepali0e.append(weakref.ref(a,callback))
 keepali0e.append(weakref.ref(lst,callback))
 keepali0e.append(weakref.ref(str,callback))
 a=A()
 a.c=a
 lst.append(a)
 lst.append(lst)
 lst.append(str())
 lst.append(a)
 lst.append(lst)
