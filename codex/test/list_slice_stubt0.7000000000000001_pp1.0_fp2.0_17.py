import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
a.a=a
keepali0e.append(a)
a.b=a
keepali0e.append(a)
try:
    weakref.finalize(a,callback,lst)
except Exception as e:
    raise RuntimeError from e
