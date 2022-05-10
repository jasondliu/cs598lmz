import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
callback(lst[0])

# exception leak
import weakref
class A(object):pass
def callback(x):pass
del lst
lst=[str()]
a=A()
a.c=a
callback(lst[0])

# memory leak for uncollectable objects
# just a few minor leaks now
keepalive=[]
for i in range(10):
    a=A()
