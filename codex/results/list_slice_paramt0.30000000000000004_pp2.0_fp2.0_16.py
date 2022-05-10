import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
gc.collect()
print lst
</code>
The output is:
<code>['', '']
</code>
I think the output should be <code>[]</code> because <code>a</code> and <code>a.c</code> are the same object.
I have tried this code on Python 2.7.5, Python 3.3.2 and Python 3.4.0.
What's wrong with this code?


A:

This is a bug in Python 2.7.5 and 3.3.2, fixed in Python 3.4.0.
The problem is that <code>a.c</code> is a cyclic reference, and <code>weakref.ref()</code> is supposed to ignore cyclic references.
The problem is that <code>weakref.ref()</code> is not ignoring cyclic references in this case.

