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
print len(keepali0e)

# other implementation

import sys
class A(object):pass
def callback(x):del lst[:]
sys.setrecursionlimit(5000)
lst=[]
a=A()
a.a=a
lst.append(weakref.ref(a,callback))
del a
print len(lst)

# other implementation

import sys
class A:pass
def callback(x):del lst[:]
sys.setrecursionlimit(5000)
lst=[]
a=A()
a.a=a
lst.append(weakref.ref(a,callback))
del a
print len(lst)

############
# -- END -- #
############
