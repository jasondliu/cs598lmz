import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive= [a, lst]
w = weakref.ref(lst, callback)

import gc
gc.collect()
del lst
gc.collect()

w()

# __new__
class A(object):
    def __new__(cls, *args, **kwargs):
        print '__new__'
        return object.__new__(cls, *args, **kwargs)
    def __init__(self, *args, **kwargs):
        print '__init__'
        super(A, self).__init__(*args, **kwargs)
        
a = A()

# __call__
class A(object):
    def __call__(self, *args, **kwargs):
        print '__call__'
        print args
        return super(A, self).__call__()
        
a = A()
a(1,2,3,4)


# __setattr__, __getattr__
class A(object):
    def __setattr__(self, name, value):
