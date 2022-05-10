import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
if len(keepali0e) != len(lst):print keepali0e[0]

print '\n--------------------'
import gc
gc.enable()
lst=[]
lst.append(lst)
print gc.collect();print gc.get_objects();print '\n'
print gc.get_referrers(lst);print '\n'
print gc.get_indexes(gc.get_objects()[0]);print '\n'
print gc.get_indexes(gc.get_objects()[3])
