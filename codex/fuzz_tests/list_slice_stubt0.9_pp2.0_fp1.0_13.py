import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
for n in range(3):
    for o in range(3):
        a.keepalive=str()
        lst.append(str())
        a.data=lst
        lst[:]
del a.data,a.c,a.keepalive,lst
gc.collect()
</code>
Output:
<code>Exception ReferenceError: "WeakMap" is not defined:
Exception ReferenceError: "WeakMap" is not defined:
Exception ReferenceError: "WeakMap" is not defined:
</code>
2:
<code>import gc
import weakref, _weakref
def callback(x):del lst[0]
lst=[str()]
for n in range(3):
    for o in range(3):
        lst.append(str())
        weakref.CallbackProxy(lst,callback).append(lst)
        lst[:]
        _weakref.ReferenceType(lst,callback)
        lst[:]
        del lst[-1]
del lst
gc.collect()
</code>
