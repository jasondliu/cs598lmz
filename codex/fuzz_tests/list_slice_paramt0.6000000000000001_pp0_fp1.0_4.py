import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
lst[0]='hello'
print len(lst)
print lst[0]

print '*'*20
import weakref
class A(object):pass
def callback(x):print 'callback',x
a=A()
a.c=a
w=weakref.ref(a,callback)
del a

print w
print w()
# w() is None
