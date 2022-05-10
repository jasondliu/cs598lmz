import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.a=weakref.ref(a,callback)
a.b=weakref.ref(a,callback)
#print(a.a,a.b,a.c)
print(a.a(),a.b(),a.c)
