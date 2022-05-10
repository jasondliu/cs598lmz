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
print(repr(keepali0e))
#[<weakref at 0x0084E8D8; to 'A' at 0x0084F5C8>, ['']]
del keepali0e
#MemoryError
#Circular reference detected
#del lst[:]
#del lst
#del keepali0e
#gc.collect()
#del lst[:]
#del lst
#del keepali0e
#gc.collect()
#del lst[:]
#del lst
#del keepali0e
#gc.collect()
#del lst[:]
#del lst
#del keepali0e
#gc.collect()
#del lst[:]
#del lst
#del keepali0e
#gc.collect()
#del lst[:]
#del lst
#del keepali0e
#gc.collect()
#del lst[:]
#del lst
#del keepali0e
#gc.collect()
#del lst[:]
#del lst
#del keepali0e

