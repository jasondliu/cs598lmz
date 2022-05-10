import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a.c
a.a=a.b
a.x=1
#a.__dict__={}
keepalive.append(a)
a.callback=callback
lst.append(a)
del a
# del keepalive
a=lst[0]
keepalive.append(a)
del lst
print(gc.collect())
print(sys.getrefcount(a))
# del keepalive
print(gc.collect())
print(sys.getrefcount(a))
