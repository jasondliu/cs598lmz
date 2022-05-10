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
'''

# EXC_BAD_ACCESS at [weakref.c line 18]
'''
import weakref
class A(object):pass
def callback(x):
    a.a
a=A()
a.a=a
keepalive=[]
keepalive.append(weakref.ref(a,callback))
del a
'''

# segfault in obj_subtype
'''
import weakref
class A(object):pass

keepalive=[]

def fn():
    a=A()
    keepalive.append(weakref.ref(a))

fn()
del keepalive[0]()
'''


# segfault in obj_subtype
'''
import weakref
class A(object):pass
class B(A):pass

keepalive=[]
a = A()
a.attr = a
keepalive.append(weakref.ref(a))
'''


# segfault in obj_subtype
'''
import weakref
class A(object):
