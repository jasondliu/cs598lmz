import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
print lst
wr=weakref.ref(a,callback)
print wr
del a
print wr
if lst:print lst,'not empty'
else:print lst,'empty'
