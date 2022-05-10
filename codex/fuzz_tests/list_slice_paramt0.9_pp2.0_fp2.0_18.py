import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst*=10**4


'''
from functools import partial
from weakref import finalize
import gc
class A(object):pass
class Foo(object):
    def __del__(self):
        import pdb;pdb.set_trace()
        print 123
def callback(x):
    print 'deleted'
    print dir(x)
    a=123
    print a
    #import pdb;pdb.set_trace()
a=A()
a.c=a
foo=Foo()
a.foo=foo
finalize(a,callback)
del a
gc.collect()
lst=partial(a)

'''
class Foo(object):
    def __del__(self):
        print 1
        import pdb;pdb.set_trace()
f1=Foo()
del f1
gc.collect()
l1=[1,2,3]
del l1
import pdb;pdb.set_trace()
import gc
import sys
class Foo(object):

