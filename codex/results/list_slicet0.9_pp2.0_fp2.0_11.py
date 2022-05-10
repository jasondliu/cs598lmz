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

KeyboardInterrupt #1442118897

# 2)
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:lst+=lst

KeyboardInterrupt #1442126968

# 3)
import weakref
class A(object):pass
keepali0e=[]
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:lst+=lst

KeyboardInterrupt #1442135213

# 4)
clas
