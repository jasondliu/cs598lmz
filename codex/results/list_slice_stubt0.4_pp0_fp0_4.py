import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
keepalive.append(a)
lst.append(a)
del a
for i in range(1000):
    x=str()
    lst.append(weakref.ref(x,callback))
    del x
    if len(lst)==1:
        break
else:
    print "error"
del keepalive[0]
del lst[0]
if len(lst)==0:
    print "ok"
