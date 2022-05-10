import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
a.c=a
keepali0e.append(weakref.ref(a))
</code>
Example #2, this code leads to segfault
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
a=2
keepali0e.append(weakref.ref(a))
</code>
I can not figure out the difference between these examples, but the first one triggers the exception and the second one leads to segfault.


A:

In the first example, the cycle is created by the line <code>a.c = a</code>.  When you execute <code>a = 2</code>, you are replacing the reference <code>a</code> refers to, but the cycle lives on.
In the second example, I assume you meant to write <code>a = A()</code> after <code>a = 2</code>. 
