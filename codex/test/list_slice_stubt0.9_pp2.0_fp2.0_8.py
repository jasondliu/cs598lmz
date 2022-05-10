import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.ccc=a
tt=a
while tt:tt.c=a;tt=tt.c
keepalive.append(a)
weakref.finalize(a,lst,callback)
del a
