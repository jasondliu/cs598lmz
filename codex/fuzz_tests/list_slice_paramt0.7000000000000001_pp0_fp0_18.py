import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
</code>
But I am getting the following error:
<code>Traceback (most recent call last):
File "&lt;stdin&gt;", line 1, in &lt;module&gt;
File "D:\Python27\lib\weakref.py", line 323, in __call__
self.callback(*arguments, **keywords)
File "&lt;stdin&gt;", line 3, in callback
ReferenceError: weakly-referenced object no longer exists
</code>
I know the behaviour of weakref module. If I change the code like this:
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
</code>
The code works. So, I am confused about the error. Can anybody help me?


A:

You're getting this error because you're deleting the weak reference from <code>keepali0e</code> when
