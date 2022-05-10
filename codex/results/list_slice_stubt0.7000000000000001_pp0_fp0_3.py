import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
b=A()
b.c=a
keepali0e.append(b)
lst.append(b)
keepali0e.append(weakref.ref(b,callback))
del a,b
for _ in range(3):
  __=lst[0]
  assert __==''
__=lst[0]
del _
gc.collect()
__=lst[0]
del __
__=lst[0]
assert keepali0e[0]()==keepali0e[1]()
__=lst[0]
del keepali0e[0]
__=lst[0]
del __,lst
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
b=A()
b.c=a
keepali0e.append(b)
lst.append(b)
keepali
