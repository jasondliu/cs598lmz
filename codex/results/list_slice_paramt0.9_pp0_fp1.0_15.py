import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print keepali0e,lst
assert len(keepali0e)==1
assert len(lst)==1
del a,lst,keepali0e
import gc
gc.collect()
print 'bad'
assert lst==['a']
print 'good'
