import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback)
del a
gc.collect()
gc.collect()
</code>
When I run it I get the following:
<code>Traceback (most recent call last):
  File "D:\Programming\Python\python-3.3.0\ref_bug.py", line 11, in &lt;module&gt;
    lst=[str()]
  File "D:\Programming\Python\python-3.3.0\ref_bug.py", line 12, in &lt;module&gt;
    a=A()
  File "D:\Programming\Python\python-3.3.0\ref_bug.py", line 13, in &lt;module&gt;
    a.c=a
TypeError: 'NoneType' object does not support item assignment
</code>
(My Python is 3.3.0, but the bug is present in both 2.7 and 3.2 as well)
What's going on?


A:

The problem is your custom "destructor" (the <code>callback</code> function). 

When
