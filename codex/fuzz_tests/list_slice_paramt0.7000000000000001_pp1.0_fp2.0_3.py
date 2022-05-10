import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
lst[0]

"""

def test(loops):
    setup = """
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
gc.disable()
for i in xrange(%d):
    del a
    gc.collect()
    lst[0]
""" % loops
    t = Timer(stmt=setup)
    r = t.repeat(repeat=1, number=1)
    return min(r)

print test(1)
