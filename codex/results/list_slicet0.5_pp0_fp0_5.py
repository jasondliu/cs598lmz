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
I'm getting this error:
<code>Traceback (most recent call last):
  File "C:\Users\Kamil\Desktop\Python\test.py", line 11, in &lt;module&gt;
    del lst[0]
RuntimeError: deallocated C object
</code>
I'm wondering why I'm getting this error and how to fix it.
I'm using Python 2.7.3 on Windows 7.


A:

The problem is that the <code>str()</code> object you're adding to <code>lst</code> is being garbage-collected before the callback function is called.
Try this instead:
<code>import weakref
class A(object): pass
def callback(x): del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst: keepali0e.append(lst[:])
</code>

