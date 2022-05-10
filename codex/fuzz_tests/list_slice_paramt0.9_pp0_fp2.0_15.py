import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
del a
for i in lst: print i
print "END"

"""

"""
#weakref bug #1
import weakref
lst=[str()]
a=1
b=2
r=weakref.ref(a)
r2=weakref.ref(b, lambda a:lst.append(a.data))
def tst():
    r2.proxy=r
    del b
    r2.proxy=None
    return 1
tst()
for i in lst:
    print i
print "END"

"""

"""
#weakref bug #2
import weakref
lst=[str()]
a=1
b=2
r=weakref.ref(a)
def tst():
    r2=weakref.ref(b, lambda a:lst.append(a.data))
    r2.proxy=r
    del b
    r2.proxy=None
    return 1
tst()
for i in lst:
    print i
print "END"

"""


