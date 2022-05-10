import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print len(keepali0e),len(lst)
del a
print len(keepali0e),len(lst)'''
def concateChar(waitlist,timeout=100):
    from time import time
    from time import sleep
    from threading import Thread
    from threading import Lock
    from threading import RLock
    from queue import Queue
    from collections import deque
    from struct import pack
    from struct import unpack
    from memory_profiler import profile
    #@profile(precision=3)
    def inner_concateChar(self,*args,**kwds):
        #from nonlocal_ import nonlocals
        preTime=time()
        throw=False
        #nonlocal timeout,timeout0,ConcateChar0,ConcateChar,waitlist,inner_concateChar
        def inner_queueChar(exception):
#            nonlocal postTime,preTime,throw,waitqueue,timeout,shutdownEvent,unpack_start,ConcateChar0,ConcateChar,waitlist,
