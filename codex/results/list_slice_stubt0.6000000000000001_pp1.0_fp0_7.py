import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
print len(lst)
print gc.collect()
print len(lst)

#del a.c
#del a.b
del a.a
print gc.collect()
print len(lst)
print gc.collect()
print len(lst)
print gc.collect()
print len(lst)
print gc.collect()
print len(lst)
print gc.collect()
print len(lst)
print gc.collect()
print len(lst)
print gc.collect()
print len(lst)
print gc.collect()
print len(lst)
print gc.collect()
print len(lst)
print gc.collect()
print len(lst)
print gc.collect()
print len(lst)

#del a.c
#del a.b
del a.a
print gc.collect()
print len(lst)
print gc.collect()
print len(lst)
print gc
