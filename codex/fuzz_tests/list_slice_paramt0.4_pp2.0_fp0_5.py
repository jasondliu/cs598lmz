import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#output:
#['<weakref at 0x000002A3E3CBE6C8; dead>']
#
#Question:
#why the ref is dead?
#why the callback is not called?
#why the list is not empty?
#
#
