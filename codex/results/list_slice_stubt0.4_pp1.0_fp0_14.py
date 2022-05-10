import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=str(a)
del a
callback(lst)
</code>
I am using python 2.7.3 and I got the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;stdin&gt;", line 7, in callback
TypeError: 'str' object does not support item deletion
</code>
I don't understand why it doesn't work. The only thing I can think of is that the <code>del</code> statement is not executed? Is there a way to force the execution of the <code>del</code> statement?


A:

<code>lst[0]</code> is a <code>str</code> object, and strings don't support item deletion.
You can use <code>del lst[:]</code> to delete all the items in the list.

