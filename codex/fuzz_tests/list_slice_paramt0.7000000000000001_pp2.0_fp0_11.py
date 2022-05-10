import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
while lst:
	time.sleep(0.1)
print "done"
'''

'''
class A(object):pass
a=A()
a.c=a
b=WeakValueDictionary()
b[1]=a
del a
print "done"
'''

'''
import weakref
class A(object):pass
a=A()
a.c=a
print a.c
print a.c.c
print a.c.c.c
print a.c.c.c.c
print a.c.c.c.c.c
print a.c.c.c.c.c.c
print a.c.c.c.c.c.c.c
print a.c.c.c.c.c.c.c.c
print a.c.c.c.c.c.c.c.c.c
print a.c.c.c.c.c.c.c.c.c.c
print a.c.c.c.
