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

# http://stackoverflow.com/questions/11238429/referencing-a-deleted-python-object-with-weakref-proxy-leaks-memory


class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
b=a
a.a=weakref.ref(a,callback)
del a
lst += [b]
while lst:
    pass
