import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
#1
keepalive=[weakref.ref(a,callback)]
for c in lst:
    keepalive.append(c)
    lst.append(str())
del keepalive
