import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a_ref=weakref.ref(a,callback)
keepalive.append(a_ref)
del a
del a_ref
print('lst=',lst)
