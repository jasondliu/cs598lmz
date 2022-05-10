import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
lst.append(a)
lst.append(a)
weakref.ref(a,callback)
del a
print lst

#print(sys.getrefcount(a))
#print(sys.getrefcount(a.c))
#print(sys.getrefcount(a.c.c))
#print(a.c.c)
#print(id(a.c.c))
#print(id(a))
#print(id(a.c))
#print(id(a.c.c))
#print(id(a))
#print(id(a.c))
#print(id(a.c.c))
#print(id(a))
#print(id(a.c))
#print(id(a.c.c))
#print(id(a))
#print(id(a.c))
#print(id(a.c.c))
#print(id(a))
#print(id(a.c))
#print(id(a.c
