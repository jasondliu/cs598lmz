import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.d=a
keepalive=[a,lst]
del a,lst
gc.collect()
lst=[str() for i in range(10000)]
lst[0]='x'
keepalive.extend(lst)
del lst
w=weakref.ref(str(), callback)
for i in range(50):
    if gc.collect():break
print 'disposing'
w=None
for i in range(50):
    if gc.collect():break
print 'disposing again'
w=None
for i in range(50):
    if gc.collect():break
print 'done'
