import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(lst)
lst.append(weakref.ref(lst,callback))
lst.append(A())
print len(lst)
del lst
print keepalive
