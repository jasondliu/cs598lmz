import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])'''

# test on str()
'''import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(weakref.ref(a,callback))
del a
while lst:keepalive.append(lst[:])'''

# test on list()
'''import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[list()]
a=A()
a.c=a
keepalive.append(weakref.ref(a,callback))
del a
while lst:keepalive.append(lst[:])'''

# test on dict()
'''import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[dict()]
a=A()
a.c=a
keepalive.append(weakref.ref
