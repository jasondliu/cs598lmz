import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print keepali0e[0]()
del a
del keepali0e
print lst

#del a.b
#print a.b
#print a.c.b
#print a.c.c.b
#print a.c.c.c.b
#print a.c.c.c.c.b
#print a.c.c.c.c.c.b
#print a.c.c.c.c.c.c.b
#print a.c.c.c.c.c.c.c.b
#print a.c.c.c.c.c.c.c.c.b
#print a.c.c.c.c.c.c.c.c.c.b
#print a.c.c.c.c.c.c.c.c.c.c.b
#print a.c.c.c.c.c.c.c.c.c.c.c.b
#print a.c.c.c.c.c.c.
