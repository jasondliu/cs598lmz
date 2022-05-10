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
print len(keepali0e)
print keepali0e

#output:
#2
#[<weakref at 0x7f7e8c0d4c18; dead>, []]

#the callback is called, but the list is not empty.
#the callback is called, but the list is not empty.
#the callback is called, but the list is not empty.
#the callback is called, but the list is not empty.
#the callback is called, but the list is not empty.
#the callback is called, but the list is not empty.
#the callback is called, but the list is not empty.
#the callback is called, but the list is not empty.
#the callback is called, but the list is not empty.
#the callback is called, but the list is not empty.
#the callback is called, but the list is not empty.
#the callback is called, but the list is not empty.
#the callback is called, but the list is not empty.
#the callback is called, but the list is not empty.
#the callback is called, but the list
