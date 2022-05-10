import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
gc.collect()
for i in range(200):
    t=weakref.ref(lst,callback)
    del t
    lst.append(str())
    del lst[0]
    if len(lst)>1:
        raise TestFailed,'leak'

class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
gc.collect()
for i in range(200):
    t=weakref.ref(lst,callback)
    del t
    lst.append(str())
    del lst[0]
    if len(lst)>1:
        raise TestFailed,'leak'

class A(object):pass
def callback(x):print "callback"
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(
