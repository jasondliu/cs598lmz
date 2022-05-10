import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
for i in range(100000):
 a1=A()
 keepali0e.append(a1)
 lst.append(a1)
 del a1
 a.c.c=a.c 
 lst.append(a)
callback(lst[0])
print "exit"
</code>
It will print "exit" in python 2.6.9. However, it will have memory leak or infinite loop in python 3.4.2. I know python 3 doesn't have dict_delitem and dict_clear, so it uses _PyDict_DelItem_KnownHash() and _PyDict_ClearFreeList() instead. However, I still can't understand why it could have memory leak or infinite loop in python 3.4.2.

