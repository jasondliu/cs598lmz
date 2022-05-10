import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
lst[0]=a
lst.append(a)
keepalive.append(lst)
keepalive.append(a)
weakref.finalize(a,callback)
</code>
It comes with this error:
<code>Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/a.py", line 2, in &lt;module&gt;
    class A(object):pass
  File "C:/Users/Administrator/Desktop/a.py", line 7, in callback
    del lst[0]
ReferenceError: weakly-referenced object no longer exists
</code>
It seems that the <code>del lst[0]</code> can't delete the object.
Why?

