import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.p=a
ref=weakref.ref(a.p,callback)
keepalive.append(ref)
del a
del keepalive[:]
while 1:print(lst)
