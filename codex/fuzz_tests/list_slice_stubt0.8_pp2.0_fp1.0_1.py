import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
b=a.c
a.c=None
print sys.getrefcount(b)
refs=[weakref.proxy(b,callback)]
print sys.getrefcount(b)
del refs[0]
print sys.getrefcount(b)
