import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.d=a
a.b=weakref.ref(a,callback)
lst=[]
a.c=a.d=a
a.b=weakref.ref(a,callback)
lst=[]
keepalive=[]
for i in range(2):
    a=A()
    keepalive.append(a)
    lst.append(str())
    a.b=weakref.ref(a,callback)
    a.c=a.d=a
    del lst[:]
