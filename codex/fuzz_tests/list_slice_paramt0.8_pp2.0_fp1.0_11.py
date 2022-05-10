import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(lst,callback))
del a
while keepali0e:keepali0e.pop()()

"""
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(lst,callback))
del a
while keepali0e:keepali0e.pop()()
"""
"""
import weakref


def callback(ref):
    print(ref)
    print(ref())
    print(type(ref))
    print(type(ref()))
    #import pdb;pdb.set_trace();
    print(ref()._ref())
    print(ref().
