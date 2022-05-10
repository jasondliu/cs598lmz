import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
del a
del a.c
del lst
gc.collect()
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
lst=[str()]
keepali0e.append(lst)
weakref.ref(a,callback)
del a
del a.c
del lst
gc.collect()
"""

def test_keepalive_2():
    source = """
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
del a
del a.c
del lst
gc.collect()
a=A()
a
