import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
weakref.ref(a,callback)
lst.append(A())
lst.append(A())
a=A()
a.lst=lst
lst.append(a)
keepalive.append(lst)
del a,lst

a=A()
a.c=a
keepalive.append(a)
a.lst=[a]
del a

#del a
e=Enum(1,2,3)
a=A()
a.c=a
keepalive.append(a)
a.lst=[e]
del a
import types
a=A()
a.c=a
keepalive.append(a)
a.lst=[types.FunctionType(lambda:1, globals())]
del a
a=A()
a.c=a
keepalive.append(a)
a.lst=[types.FrameType]
del a
import sys
a=A()
a.c=a
keepalive.append(a)

