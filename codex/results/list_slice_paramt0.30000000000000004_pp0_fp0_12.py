import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
print lst

#第二个例子
import weakref
class A(object):pass
def callback(x):print "callback"
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
print "over"

#第三个例子
import weakref
class A(object):pass
def callback(x):print "callback"
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
print "over"

#第四个例子
import weakref
class A(object):pass
def callback(x):print "callback"
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))

