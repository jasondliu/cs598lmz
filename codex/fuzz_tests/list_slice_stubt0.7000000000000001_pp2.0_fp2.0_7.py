import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(a)
del a
for i in range(1000):
    a=A()
    a.c=a
    lst.append(a)
    weakref.ref(a,callback)
    del a
    if len(lst)==1:break
else:
    print("Did not see expected behavior")
</code>
This prints:
<code>&gt;&gt;&gt;
</code>

