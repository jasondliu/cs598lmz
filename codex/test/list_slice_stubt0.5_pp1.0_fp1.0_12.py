import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=a
lst.append(a)
keepalive=[]
lst.append(weakref.ref(a,callback))
keepalive.append(lst)
del lst,keepalive
