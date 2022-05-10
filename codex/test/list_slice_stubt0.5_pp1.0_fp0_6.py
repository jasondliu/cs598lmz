import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
wref=weakref.ref(a,callback)
keepali0e.append(wref)
assert wref() is a
