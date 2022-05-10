import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
lst.append(a)
keepalive=[a]
b=A()
b.c=b
b.d=b
lst.append(b)
keepalive.append(b)
weakref.finalize(a,callback,b)
print lst
