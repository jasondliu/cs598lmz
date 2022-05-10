import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst[0].callback=callback
lst[0].callback=lambda x:None
print(len(keepali0e))
</code>

