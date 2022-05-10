import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(lst,callback))
lst.append(a)
del a
del lst
print "If the previous line is 'TypeError: list indices must be integers' instead of 'Traceback (most recent call last):' then there is a bug in Python in which list.__delitem__ is not called when an item is removed by weakref.ref callback."
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[A()]
lst[0].c=lst
keepali0e.append(weakref.ref(lst,callback))
lst.append(str())
del lst
print "If the previous line is 'TypeError: list indices must be integers' instead of 'Traceback (most recent call last):' then there is a bug in Python in which list.__delitem__ is not called when an item is removed by weakref.ref callback."
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[A()
