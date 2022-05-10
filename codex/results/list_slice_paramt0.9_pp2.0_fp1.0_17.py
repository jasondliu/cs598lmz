import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a.b=a
del keepali0e[0]
del lst[0]
del a
</code>
According to the documentation, a dead object should take a circular reference after gc.collect(). I know,that weak reference is unusable, but that's not the issue. The issue is, it will never go out of memory and I can't use a circular dependency to test the memory. Is this a bug, or is it by design? Here is proof, according to my profiler:
https://imgur.com/a/YmYcjmC
I am using python 3.6. I also tried python 2.7 and python 3.7. None of them behaves differently, and none of them shows memory increase on Linux or Windows. So if this is a feature, then why is it there for and how is it supposed to be used?


A:

Ah, it was indeed a profiler problem. I used Cpython profiler and the numbers of elements in the list was decreasing instead of increasing. However, using Asyncio and using memory profiler from here: https://github.com/pythonprofilers/memory_
