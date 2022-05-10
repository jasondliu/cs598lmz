import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(a)
w=weakref.ref(a,callback)
for i in range(5):print(i,lst)

print(lst)
import gc
gc.collect()
print(lst)

## ------------------------------------- ##
from random import choice,randint
import weakref
class A(object):pass
def make_callback(x):
        def func():
                print("deleting object at address 0x{:x} in callback!"
                        .format(id(x)))
                del lst[0]
        return func
lst=[]
for i in range(10):
    a=A()
    lst.append(a)
    lst.append(weakref.ref(a,make_callback(a)))
    lst.append(a)
    lst.append(randint(0,3))
    lst.append(choice("abc"))
while lst:
    lst.pop()
print("len(lst) =",len(lst))

