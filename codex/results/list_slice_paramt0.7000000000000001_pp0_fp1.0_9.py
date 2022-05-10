import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
a=None
print(lst)
import weakref
class A(object):pass
a=A()
a.c=a
r=weakref.ref(a)
print(r())
a=None
print(r())
