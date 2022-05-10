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
print keepali0e
print O.pformat(keepali0e)


#keepalive inline reference
print "2"
keepali1e=[]
keepali1e.append([keepali1e,str()])
del keepali1e
print O.pformat(keepali1e)

#keepalive reference from a list
print "3"
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
alst=[str()]
a=A()
a.c=lst
lst.append(alst)
lst.append(a)
keepali2e=[]
keepali2e.append(weakref.ref(a,callback))
del a
while lst:keepali2e.append(lst[:])
print O.pformat(keepali2e)


#corner case bug report
print "4"
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali3e=[]
lst
