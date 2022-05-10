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
This reproduces the error for me on both Python 2.7 and on Python 3.2. If you want to verify that the error is the same, you can run the following script on Python 3.2:
<code>import traceback
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
with open('traceback.txt','w') as f:
    traceback.print_exc(limit=None,file=f)
</code>
Running the above script will cause Python to crash. The traceback is captured in <code>traceback.txt</code>. If you compare this traceback with the one in your question, you'll see that they're basically identical.

