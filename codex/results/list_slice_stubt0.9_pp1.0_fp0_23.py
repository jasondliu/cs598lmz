import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
print lst
del lst
keepalive.append(lst)
weakref.ref(lst[0],callback)
print len(lst)
