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
del lst
del keepali0e
print "ok"
"""
"""
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
a.c=a
del a
while lst:keepali0e.append(lst[:])
del lst
del keepali0e
print "ok"
"""

#Expected crash
"""
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
a.c=a
del a
while lst:keepali0e.append(lst[:])
del lst
del keepali0e
print "ok"
"""

#
"""
import weakref
class A(object):pass
def callback(x):del l
