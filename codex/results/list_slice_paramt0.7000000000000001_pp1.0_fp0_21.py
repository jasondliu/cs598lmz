import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))

for i in range(0,1):
    keepali0e.append(weakref.ref(a,callback))
    a=None
    lst.append(str())
keepali0e.append(weakref.ref(a,callback))
print 'done'
