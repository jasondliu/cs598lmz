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
'''

manipulate_code='''
import weakref
class A(object):pass
def callback(x):x.c=None
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a.c=None
del a
while lst:keepali0e.append(lst[:])
'''

class Leak(object):
    """Class used to find un-reachable circular references"""
    def __init__(self,obj,iter_limit_=1024):
        self.iter_limit=iter_limit_
        self.keep_alive=[]
        self.refs=[]
        self.seen=[]
        self.queue=[obj]
        self.obj=obj

    def collect(self):
        wr=weakref.ref
        queue=self.queue
        keepalive=self.keep_alive
        get=self.obj.__class__.__getattribute__
        seen=self.seen
