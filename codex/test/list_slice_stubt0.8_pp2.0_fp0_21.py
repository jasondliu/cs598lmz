import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(a.c,callback))
for x in range(len(lst)):keepali0e.append(str())
del x
del a
del callback
while lst:pass
