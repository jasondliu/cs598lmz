import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
keepali0e.append(weakref.ref(lst[0]))
del a
del lst
keepali0e.append(weakref.ref(str()))
gc.collect()
for i in keepali0e:print i
del keepali0e
print gc.collect()
"

#
#  test_memo_in_new_thread
#

test_memo_in_new_thread="""
import gc
import threading
import time
import weakref
def f():
    a=A()
    a.c=a
    keepalive=[]
    keepalive.append(weakref.ref(a))
    keepalive.append(weakref.ref(a.c))
    del a
    time.sleep(3)
    gc.collect()
    for i in keepalive:print i
    del keepalive
    print 'gc:', gc.collect()
class A(object):pass
a=A()
