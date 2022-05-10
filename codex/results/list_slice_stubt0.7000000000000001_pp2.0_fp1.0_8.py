import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a #make a cyclic object
keepalive.append(a)
lst[0]=a # make a reference cycle
weakref.ref(lst,callback)
keepalive.remove(a)
print lst[0] # no callback should be called
