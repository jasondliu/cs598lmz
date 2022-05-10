import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
t1=threading.Thread(target=lambda:keepalive(lst[0],callback,0))
t2=threading.Thread(target=lambda:id(weakref.proxy(a)))
t1.start()
t2.start()
t1.join()
t2.join()

"""
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
t1=threading.Thread(target=lambda:keepalive(lst[0],callback,0))
t2=threading.Thread(target=lambda:id(weakref.proxy(a)))
t1.start()
t2.start()
t1.join()
t2.join()

"""
"""
#Can be used by using with statement which can handle exception
#elimate the need for calling close
#allow file to be opened on multiple tehreads

#threading.Lock
import threading
lock=threading.Lock()
lock.
