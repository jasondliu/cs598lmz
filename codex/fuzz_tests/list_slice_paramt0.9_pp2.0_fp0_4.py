import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
lst

class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[A()]
a=A()
a.c=a
keepalive.append(weakref.ref(a, callback))
lst
lst[0].x=lst
del lst
del keepalive
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[A()]
a=A()
a.c=a
keepalive.append(weakref.ref(a, callback))
lst
del lst[0]
keepalive
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[A()]
a=A()
a.c=a
keepalive.append(weakref.ref(a, callback))
lst
del keepalive[:]
lst
a.c
lst
class A(object):pass
def callback(x):del
