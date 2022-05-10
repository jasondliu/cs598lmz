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
del keepali0e

#keepalive=[]
#lst=[str()]
#a=A()
#a.c=a
#keepalive.append(weakref.ref(a,callback))
#del a
#while lst:keepalive.append(lst[:])
#del keepalive

#keepalive=[]
#lst=[str()]
#a=A()
#a.c=a
#keepalive.append(weakref.ref(a,callback))
#del a
#while lst:keepalive.append(lst[:])
#del keepalive

#keepalive=[]
#lst=[str()]
#a=A()
#a.c=a
#keepalive.append(weakref.ref(a,callback))
#del a
#while lst:keepalive.append(lst[:])
#del keepalive

#keepalive=[]
#lst=[str()]
#a=A()
#a.c=a

