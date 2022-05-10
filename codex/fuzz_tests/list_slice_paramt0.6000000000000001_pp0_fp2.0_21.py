import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
keepali0e.append(weakref.ref(lst,callback))
del lst
</code>
The above code works perfectly. But the following code(only difference is the way the callback function is defined) doesn't work,and produces an error:
<code>import weakref
class A(object):pass
def callback(x):
    del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
keepali0e.append(weakref.ref(lst,callback))
del lst
</code>
The error produced is:
<code>Traceback (most recent call last):
  File "C:\Users\User\Desktop\python\weakref\weakref_callback.py", line 13, in &lt;module&gt;
    del lst[0]
NameError: name 'lst' is not defined
</code>
Can you please explain the working of the first code and the
