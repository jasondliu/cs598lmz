import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a,lst
keepali0e.append(a)
keepali0e.append(lst)
lst[0]=lst
#del lst
#del a
print a.c
#gc.collect()
print a.c

#gc.disable()
del a
del lst
#gc.enable()
gc.collect()
