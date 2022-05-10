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
print(keepali0e)

#print(lst)

#print(a)
#print(a.c)
#print(a.c.c)
#print(a.c.c.c)
#print(a.c.c.c.c)
#print(a.c.c.c.c.c)
#print(a.c.c.c.c.c.c)
#print(a.c.c.c.c.c.c.c)
#print(a.c.c.c.c.c.c.c.c)
#print(a.c.c.c.c.c.c.c.c.c)
#print(a.c.c.c.c.c.c.c.c.c.c)
#print(a.c.c.c.c.c.c.c.c.c.c.c)
#print(a.c.c.c.c.c.c.c.c.c.c.c.c)
#print(
