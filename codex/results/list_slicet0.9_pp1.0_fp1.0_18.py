import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

#list memory leak
import weakref
class A(object):pass
lst=[]
a=A()
a.c=a
lst.append(weakref.ref(a))
del a
while lst:lst.pop().__call__()

#what's the locale
import locale
print(locale.getdefaultlocale())
