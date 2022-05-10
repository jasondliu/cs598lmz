import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
callback(lst[0])

# exception leak
import weakref
class A(object):pass
def callback(x):pass
del lst
lst=[str()]
a=A()
a.c=a
callback(lst[0])

# memory leak for uncollectable objects
# just a few minor leaks now
keepalive=[]
for i in range(10):
    a=A()
    b=B()
    c=C()
    a.x=b
    b.x=c
keepalive=[]
del a,b,c

# memory leak when an exception occurs with a callback
import weakref

def callback(x):
    raise Exception()

class A(object):pass

a=A()
a.x=a
wr=weakref.ref(a,callback)
"""

class TestLeak(object):
    def setup_class(cls):
        cls.w_tmpdir = cls.space.appexec([], """():
    import os
    return os.path.abspath
