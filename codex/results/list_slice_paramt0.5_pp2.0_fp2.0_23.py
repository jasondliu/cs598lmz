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
del keepali0e
print lst
# output:
# ['1']
# []

#example 4
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print lst
del keepali0e
print lst
# output:
# ['1']
# []

#example 5
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del keepali0e
del a
print lst
# output:
# ['1']

#example 6
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
keepali
