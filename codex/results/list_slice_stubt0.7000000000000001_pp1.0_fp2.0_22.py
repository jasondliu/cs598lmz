import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append((a,a))
keepali0e.append(a)
a.e=lst
keepali0e.append(a)
del a
del lst
def f1(i=keepali0e):
    lst2=[]
    lst2.append(i[0])
    lst2.append(i[1])
    return lst2
def f2(i=keepali0e):
    lst2=[]
    lst2.append(i[0])
    lst2.append(i[1])
    return lst2
f1()
f2()

#g_cycle_finalizer_lock=_thread.allocate_lock()
#g_cycle_finalizer_lock.acquire()
#g_cycle_finalizer_lock.release()

#gc.callbacks.append(callback)
