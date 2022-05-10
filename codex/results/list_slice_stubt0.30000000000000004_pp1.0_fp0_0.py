import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
weakref.ref(lst[1],callback)
del lst
del keepalive
import gc
gc.collect()

#结果：
#gc: collectable <list 0x7f2a2a8e9e48>
#gc: collectable <A 0x7f2a2a8e9f28>
#gc: collectable <A 0x7f2a2a8e9f28>
#gc: collectable <list 0x7f2a2a8e9e48>
#gc: collectable <A 0x7f2a2a8e9f28>
#gc: collectable <list 0x7f2a2a8e9e48>
#gc: collectable <A 0x7f2a2a8e9f28>
#gc: collectable <list 0x7f2a2a8e9e48>
#gc: collectable <A 0x7f2a2a
