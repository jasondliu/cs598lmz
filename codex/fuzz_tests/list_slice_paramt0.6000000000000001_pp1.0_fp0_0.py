import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
gc.collect()
print lst
lst.append(str())
gc.collect()
print lst

import gc,weakref
class A(object):
    def __del__(self):
        print 'A.__del__'
        gc.collect()
        print 'A.__del__'
class B(object):
    def __del__(self):
        print 'B.__del__'
a=A()
b=B()
a.c=b
b.c=a
del a
gc.collect()
print 'end'

import gc,weakref
class A(object):
    def __del__(self):
        print 'A.__del__'
        gc.collect()
        print 'A.__del__'
class B(object):
    def __del__(self):
        print 'B.__del__'
a=A()
b=B()
a.c=b
b.c=a
del a,b
gc.collect()
print 'end'
