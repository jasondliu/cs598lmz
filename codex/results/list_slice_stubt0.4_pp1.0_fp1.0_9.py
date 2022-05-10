import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
keepali0e.append(lst[0])
del a,lst
gc.collect()
print(len(gc.get_objects()))
</code>
The output is:
<code>13
</code>

