import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))

for i in range(2):
    keepalive.append(lst)
    lst=lst[0]
del keepalive
gc.co1lect()
