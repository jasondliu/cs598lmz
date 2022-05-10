import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(lst)
keepalive.append(callback)
a.x=callback
del keepalive
del a
trash=[]
for s in range(2):w=weakref.ref(str(),callback);trash.append(w)
for s in range(2):w=weakref.ref(str(),lambda x:x);trash.append(w)

# change sys.exc_clear() to be always called by gc during gc collection
import sys,gc,itertools
class CallCount(object):
  def __init__(self,func):
    self.func=func
    self.calls=0
    self.calls=[func,self.calls]
  def __call__(self,*args,**kwargs):
    ret=apply(self.func,args,kwargs)
    self.calls[1]+=1
    return ret
sys.exc_clear=CallCount(sys.exc_clear)
gc.callbacks=[]
gc.callbacks.append(lambda:id(int))
gc
