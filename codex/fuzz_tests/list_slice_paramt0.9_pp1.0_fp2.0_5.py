import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a,A
</code>
circular references, to avoid the ancient crasher:
<code>for i in range(1000000):lst.append(str())
</code>
After some time, the timer event below will drop the circular reference and free the 'a' instance. 
This is the main event loop.
<code>from threading import Event
event=Event()
def timer():
    global event
    event.set()
from threading import Timer
t=Timer(5,timer)
t.start()
while not event.is_set():
    event.wait()
t=None
</code>
I find that the weak reference callback hasn't been called, and I see a't' object still alive from a refcount debug tool.
What does Python do ?


A:

First things first, your use of Timer is questionable, because the timer threading is effected by main threading. This will not work reliabily, if at all. 
See this similar question's answers.
The weak reference, is probably working; while you're waiting. If
