import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
for i in range(100):
  gc.collect()
gc.disable()
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
for i in range(100):
  gc.collect()
print len(gc.garbage)
print gc.garbage
print len(gc.garbage)
print gc.garbage
print len(gc.garbage)
print gc.garbage
