import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(lst)
lst[0]=lst
del lst
del keepalive
gc.collect()
print all_objects
</code>
I am using python 3 and I was expecting <code>all_objects</code> to be empty since I deleted everything.
However, the code above is printing <code>[[b'', &lt;__main__.A object at 0x10d32e128&gt;]]</code> in my machine.
The question is why?


A:

Don't use <code>weakref.all_objects()</code> for this. <code>all_objects()</code> is a debug tool; it's not meant to be used in production code. It is slow, and it holds references to everything in memory to build the list.
You can't, in general, determine if an object is still alive. The only way to do this is to keep a reference to the object, but if you keep a reference then the object will be alive.
If you need to determine if an object is still alive, then use a <code
