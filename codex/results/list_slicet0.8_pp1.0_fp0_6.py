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
I'm running this code on Python 3.2 on Windows. In the past I've seen this and similar codes run forever.
So what could cause it? Maybe the memory model or the garbage collector? Or some other library, like the logging module, doing something in the background?


A:

Honestly, I don't think that this is a robust test.  You haven't even waited for the garbage collector to kick in.
I would recommend using the <code>gc</code> module and actually checking for garbage.  It is also possible that your code is leaking references to other objects.
This is a hacked version of your code which works fine on my machine:
<code>import gc
import weakref
import time

class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:
    keepali0e.append(lst[:])
    time.sleep(0.050)
