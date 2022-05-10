import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a1
#callback(a)
keepalive=weakref.ref(a,callback)
print lst
#print a.c
'''
class A(object):
    pass
a=A()
a.c=a1
 
 
 
def callback(x):
    print 'Deleted by WeakRef'
    del lst[:]
pr0nt keepalive
lst=[44,66]
keepalive=weakref.ref(a,callback)
print lst
'''
