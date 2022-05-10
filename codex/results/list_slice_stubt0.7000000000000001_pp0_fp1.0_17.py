import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append(weakref.ref(a,callback))
lst.append(keepalive)
del a
del lst
for i in range(300):
    keepalive.append(str())
print('Finished')
