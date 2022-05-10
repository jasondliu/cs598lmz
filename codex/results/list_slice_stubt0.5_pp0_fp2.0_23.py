import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
lst[0]=weakref.ref(lst[0],callback)
print(len(keepalive))

import weakref
class A(object):pass
lst=[str()]
a=A()
a.c=a
lst[0]=a
lst[0]=weakref.ref(lst[0],lambda x:del lst[0])
print(len(keepalive))
