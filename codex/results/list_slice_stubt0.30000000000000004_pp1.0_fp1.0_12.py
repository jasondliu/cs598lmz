import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
lst.append(a)
del a
keepali0e.append(lst)
del lst
gc.collect()
print(keepali0e)

#weakref.ref(a,callback)
#del a
#gc.collect()
#print(lst)
#print(lst[0])
#print(lst[1])
#print(lst[1].c)
#print(lst[1].c.c)
#print(lst[1].c.c.c)
#print(lst[1].c.c.c.c)
#print(lst[1].c.c.c.c.c)
#print(lst[1].c.c.c.c.c.c)
#print(lst[1].c.c.c.c.c.c.c)
#print(lst[1].c.c.c.c.c.c.c.c)
#print(lst[1].c.c.c.
