import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
keepali0e.append(weakref.ref(lst))
lst[0]=lst
keepali0e.append(weakref.finalize(a,callback))
try:
    del a
    del a.c
    del lst
    gc.collect()
    print 1
except ReferenceError:
    print 2
</code>
Output:
<code>2
</code>

