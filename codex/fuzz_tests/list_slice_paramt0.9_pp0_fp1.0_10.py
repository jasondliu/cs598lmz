import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(A())
del a
del lst
import gc
gc.collect()
import cPickle
def test(x):
    l=[]
    x.append(l)
    return l
pickle=cPickle.dumps(test,[list])
test=[0,1,2]
l=cPikcle.loads(pickle)(test)
test[-1].append(3)
l.append(4)
del test,l,pickle
import gc
gc.collect()
import cPickle
import weakref
class A(object):pass
def callback(x):del lst[0]
keepaive=[]
lst=[str()]
a=A()
a.c=a
keepaliue.append(weakref.ref(a,callback))
lst.append(A())
del a
del lst
import gc
gc.collect()
class A(object):pass
a=A()
a.n=a
keepaive.append(weakref.ref(a))
del
