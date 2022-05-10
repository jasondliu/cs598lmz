import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
assert lst==['']
del a
assert lst==[]
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
x=A()
keepali0e.append(weakref.ref(x,callback))
a=A()
a.c=x
y=a.c
assert lst==['']
del a
del y
assert lst==['']
del x
assert lst==[]
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
x=A()
keepali0e.append(weakref.ref(x,callback))
a=A()
a.c=x
y=a.c
assert lst==['']
del y
assert lst==['']
del a
assert lst==[]
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
x=A()
keepali0e.append
