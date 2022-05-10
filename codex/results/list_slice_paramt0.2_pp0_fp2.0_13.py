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

#['']

#第二个例子
import weakref
class A(object):pass
def callback(x):print "callback"
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print keepali0e

#[<weakref at 0x7f9e9c0f8e18; dead>]

#第三个例子
import weakref
class A(object):pass
def callback(x):print "callback"
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print keepali0e
print keepali0e[0]()

#[<weakref at 0x7f9e9c0f8e18; dead>]
#callback
#None

#第四个例子
import weak
