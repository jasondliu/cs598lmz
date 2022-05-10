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
print(len(keepali0e))"""
"""def oka():
    k=str()
    lst=[k]
    a=A()
    assert a.x is None
    a.x=a
    lst.append(a)
    del a
    del k
while lst: keepali0e.append(lst[:])   

for _ in range(10000):oka()
print(len(keepali0e),len(lst))"""
#keepali0e,lst=[],[str()]
"""for _ in range(10000):
    a=A()
    a.x=a
    lst.append(a)
    del a

for _ in range(10000):
    k=str()
    lst.append(k)
    del k"""
#print(len(keepali0e),len(lst))
"""keepali0e,lst=[],[str()]
for _ in range(10000):
    a=A()
    a.x=a
    lst.append(a)
    del a
