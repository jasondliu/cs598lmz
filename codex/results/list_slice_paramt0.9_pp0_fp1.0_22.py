import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
x=list(lst)
print(x)
</code>


A:

Is the reason there is no output because the <code>print(x)</code> line is supposed to be <code>print(x[0])</code>?
If so, consider using <code>repr()</code> rather than <code>str()</code>. As it is, when your <code>str()</code> is converted to a list object you have no way to display that object.
<code>from __future__ import print_function
import weakref
class A(object): pass
def callback(x): del lst[0]
keepalive=[]
lst = [repr('The quick brown fox jumped over the lazy dog')]
a = A()
a.c = a
keepalive.append(weakref.ref(a,callback))
del a
x = list(lst)
print(x[0])
</code>

