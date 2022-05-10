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

#[<weakref at 0x7f0b8c7a6f78; to 'A' at 0x7f0b8c7a6f28>, []]
