import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.l=lst
keepalive=lst
del a
#del lst
class B(object):
    def __init__(self):self.cb=weakref.WeakMethod(callback,callback_ref=callback)
    def __del__(self):self.cb()
