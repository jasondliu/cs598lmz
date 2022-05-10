import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=lst
lst[0]=weakref.ref(lst,callback)
del lst
lst=[]
for i in range(10):
    a=A()
    a.c=a
    lst.append(a)
    keepalive.append(a)
    del a
del lst
import gc
gc.collect()
print(gc.garbage)

#[<__main__.A object at 0x7f5c8d0b8f28>, <__main__.A object at 0x7f5c8d0b8f98>, <__main__.A object at 0x7f5c8d0b8f60>, <__main__.A object at 0x7f5c8d0b8f28>, <__main__.A object at 0x7f5c8d0b8f98>, <__main__.A object at 0x7f5c8d0b8f60>, <__main__.A object at 0
