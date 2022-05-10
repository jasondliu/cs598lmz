import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst,callback))
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(lst))
keepali0e.append(str())
keepali0e.append(str())
del a
print(lst)
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
keepali0e=weakref.WeakKeyDictionary()
keepali0e[a]=lst
keepali0e[lst]=a
print(lst)
del a
print(lst)
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
keepali0e=weakref.WeakValueDictionary()
keepali0e[a]=lst
keepali0e[lst]=a
print(lst)
del
