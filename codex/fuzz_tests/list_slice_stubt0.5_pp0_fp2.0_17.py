import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=a
keepalive.append(a)
a.a=weakref.ref(a,callback)
lst.append(a)
print lst
#[str(), <__main__.A object at 0x7f7e9d07c6d0>]
print len(lst)
#2
del a
#callback(a.a)
print lst
#[str()]
print len(lst)
#1
