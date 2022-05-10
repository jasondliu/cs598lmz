import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=[]
keepalive.append(a)
wf=weakref.ref(a,callback)
