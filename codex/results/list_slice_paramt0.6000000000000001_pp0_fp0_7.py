import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
print len(lst)
</code>
This code prints 0, which is what I want. But I'm not sure if it's correct.

