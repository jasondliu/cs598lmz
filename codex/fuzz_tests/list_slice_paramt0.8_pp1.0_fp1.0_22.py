import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
c_count=0
while lst:
    c_count+=1
for i in range(2):
    lst=[str()]
    a=A()
    a.c=a
    keepali0e.append(weakref.ref(a,callback))
    del a
while lst:
    c_count+=1
print 'c_count=',c_count
