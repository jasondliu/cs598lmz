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
I also tried this version, which is a more direct attempt to get the same thing:
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(list(lst))
</code>
but it also fails.
I am using Python 3.7.0 on Windows 10.
What is going on here?


A:

The problem is with the <code>lst</code> list.
<code>lst = [str()]
</code>
This creates a list containing a single <code>str</code> object, which is empty. The list is empty, but it contains a single item, an empty string.
When you append <code>lst</code> to <code>keepali0e</code>, you append a reference to the list. The list itself is not a copy of <
