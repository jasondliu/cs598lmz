import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
weakref.ref(a,callback)
del a
keepalive.append(lst)
</code>
And this is the error message I get:
<code>Traceback (most recent call last):
  File "C:\Users\HP\Desktop\cpython\Demos\weakref_callback.py", line 14, in &lt;module&gt;
    weakref.ref(a,callback)
TypeError: cannot create weak reference to 'A' object
</code>
I don't know why this error occurs.

