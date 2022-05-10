import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a_weakref=weakref.ref(a,callback)
keepali0e.append(a)
print keepali0e

del a
for i in range(5):
    print i,':',lst
    pass
print 'over'
