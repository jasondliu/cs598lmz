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
The error is:
<code>Traceback (most recent call last):
  File "C:/Users/matt/Desktop/Python/python.py", line 11, in &lt;module&gt;
    del a
NameError: name 'a' is not defined
</code>
I don't understand why the error is appearing, because <code>a</code> was defined.

