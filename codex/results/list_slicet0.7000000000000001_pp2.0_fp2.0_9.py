import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
</code>
If the list <code>lst</code> is empty, the program terminates. Else, it goes into an infinite loop.
In the case that I have a memory leak, the <code>lst</code> list will have the string <code>str()</code> in it. As expected, when I run this code, it never terminates. However, when I run it with a memory profiler, the list <code>lst</code> is being cleared. I suspect it might be related to the fact that there's no <code>gc.collect</code> between the <code>keepalive.append</code> and the <code>del a</code>.
Is there a way to force a call to the garbage collector? If not, am I missing something that would explain why the list <code>lst</code> is being cleared?


A:

The issue is that <code>sys.getrefcount</code> is not reliable. You can check it out here. There is no way to force a call to the garbage collector in python. This can be seen here. So I suggest you to use a better prof
