import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
lst.append(lst[0])
del a
del keepalive[0]
print(lst)

#析构顺序
a=A()
b=A()
a.b=b
b.a=a
del a
del b

#析构顺序
from weakref import ref
class A(object):pass
a=A()
b=A()
a.b=ref(b)
b.a=ref(a)
del a
del b

#析构顺序
from weakref import ref
class A(object):pass
a=A()
b=A()
a.b=ref(b)
b.a=ref(a)
a=b=None

#析构顺序
from weakref import ref
class A(object):pass
a=A()
b=A()
a.
