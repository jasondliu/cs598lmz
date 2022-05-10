import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
a.b=lst
a.a=weakref.ref(a,callback)
del a
print('lst:',lst)
del lst
print('keepalive:',keepali0e)
