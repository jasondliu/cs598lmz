import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
lst[0]='bbb'
b=A()
lst[0]=weakref.ref(b,callback)
b.c=b
keepali0e.append(b)
del b
del a
from gc import collect
collect()
from gc import collect
collect()
del keepali0e
from gc import collect
collect()
