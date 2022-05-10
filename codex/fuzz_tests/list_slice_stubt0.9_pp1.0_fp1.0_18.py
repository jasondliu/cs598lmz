import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
print id(a),id(a.c)
a=None
a1=lst[0]#should has strong refernce from lst[0]
b1=str()
print id(a1),id(b1)
print 'Before:'
for obj in gc.get_objects():
    print obj, type(obj)
del a1
print 'After:'
for obj in gc.get_objects():
    print obj, type(obj)
import ctypes
x,y=1,2
print ctypes.addressof(x)
print ctypes.addressof(y)
