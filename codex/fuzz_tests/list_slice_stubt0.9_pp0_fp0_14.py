import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
final=lst[0]
del lst
weakref.finalize(final,callback)
print(bool(final))
keepalive=[]
final=None
weakref.cleanup_cycle()
print(bool(final))
