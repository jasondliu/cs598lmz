import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
for n in range(10):keepalive=weakref.ref(a,callback)
keepalive=None
del a
a=A()
a.c=a
for n in range(10):keepalive=weakref.ref(a,callback)
keepalive=None
del a
while len(lst)>0:import gc;gc.collect()
del lst
del keepalive
del a
del callback
del A
lst=[]
del lst
import sys
import weakref
class A(object):
    def __init__(self,callback):
        self.callback=callback
    def __del__(self):
        self.callback()
def callback():
    sys.stdout.write('.')
    sys.stdout.flush()
    if len(lst)==0:
        import threading
        threading.Thread(target=shutdown).start()
lst=[A(callback)for n in range(10)]
del lst
import sys
import weakref
