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
del keepali0e
print len(lst)

# this program will print 1, but in python2.4.4 it will print 0
# it's because when a is deleted, the callback function is called, but a.c is still alive, so the callback function is called
# again and the list is empty.
# in python2.4.4, the callback function is not called again, so the list is not empty.
# I think the python2.4.4 is right.
