import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
del a
gc.collect()
print lst

#[<__main__.A object at 0x7f8e8c0>]

#lst[0] is a weak reference to the object a.
#The object a has a reference to itself, so it is not collected.
#The weak reference is not collected, because it is in the list lst.
#The list lst is not collected, because it is referenced by the local variable lst.
#The local variable lst is not collected, because it is referenced by the function callback.
#The function callback is not collected, because it is referenced by the weak reference lst[0].
#The weak reference lst[0] is not collected, because it is in the list lst.
#The list lst is not collected, because it is referenced by the local variable lst.
#The local variable lst is not collected, because it is referenced by the function callback.
#The function callback is not collected, because it is referenced by the weak reference lst[0].
#The weak
