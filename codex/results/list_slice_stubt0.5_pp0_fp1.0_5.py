import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(lst)
wr=weakref.ref(lst,callback)
del keepalive[:]
del a
print lst
print wr
print wr()
del lst
print wr
print wr()
