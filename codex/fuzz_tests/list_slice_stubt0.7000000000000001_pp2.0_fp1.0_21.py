import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepali0e.append(weakref.ref(lst[0],callback))
del a
del lst
</code>
Here is the code I use to test the issue:
<code>import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepali0e.append(weakref.ref(lst[0],callback))
del a
gc.collect()
print(lst[0])
</code>
I have a break point in the callback. When I run the code, the callback is invoked, but when I print lst[0], it is still there. How can I remove the object from lst when the callback is invoked?
Thanks a lot!


A:

The weakref is being called. But you aren't actually removing anything from the list. 
<code>def callback(x):del lst[0]
</code>
is the same
