import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
keepalive=[a,b]
while len(lst)>0:
    keepalive.append(weakref.ref(A(),callback))
    keepali0e.append(keepalive[-1]())
    keepali0e.append(keepali0e[-1].c)
print "end"
