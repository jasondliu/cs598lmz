import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst.append(weakref.ref(lst,callback))
keepalive.append(lst)
del lst
del keepalive
"""

test_cpython_3 = """
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst.append(weakref.ref(lst,callback))
keepalive.append(lst)
del lst
del keepalive
"""

test_pypy_1 = """
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst.append(weakref.ref(lst,callback))
keepalive.append(lst)
del lst
