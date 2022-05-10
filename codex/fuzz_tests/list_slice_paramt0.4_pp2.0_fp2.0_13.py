import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#output
#['<weakref at 0x0000000002B8B8B8; to 'A' at 0x0000000002B8B848>']

#example 2
import weakref
class A(object):pass
def callback(x):print "callback"
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#output
#callback
#['<weakref at 0x0000000002B8B8B8; dead>']

#example 3
import weakref
class A(object):pass
def callback(x):print "callback"
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#output
#callback
#['<weakref at 0x0000000002B8B8B8; dead>']
