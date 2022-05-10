import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append(a)
keepalive=list(lst)
lst.append(weakref.ref(lst[1], callback))
a=None
