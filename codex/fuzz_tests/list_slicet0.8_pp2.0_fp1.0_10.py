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

#test10
class A(object):pass

def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

#====================
#====================

#test11
class A(object):pass

def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
keepalive.append(a)
keepalive.append(weakref.ref(a,callback))
del a
while lst:keepalive.append(lst[:])

#test12
class A(object):pass

def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
keepalive.append(a)
a.c = a
keepalive.append(weakref.ref(a,
