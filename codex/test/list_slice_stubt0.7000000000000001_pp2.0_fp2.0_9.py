import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=a
lst.append(a)
keepalive=lst
callback_ref=weakref.ref(callback,callback)
print(callback_ref)
print(callback_ref())
keepalive=callback
print(callback_ref())
callback_ref=None
keepalive=None
print(lst)
