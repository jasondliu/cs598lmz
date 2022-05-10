import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
</code>
but I get an error:
<code>Traceback (most recent call last):
  File "&lt;pyshell#0&gt;", line 1, in &lt;module&gt;
    del lst[0]
RuntimeError: dictionary changed size during iteration
</code>
I don't understand why the dictionary is being modified during iteration.

