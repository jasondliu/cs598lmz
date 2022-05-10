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
for i in lst:
    print(i)
</code>
my question is why the output is <code>None</code>?
my expect is print <code>&lt;weakref at 0x0000000002CCF448; to 'A' at 0x0000000002CCF4E0&gt;</code>
why <code>lst</code> is empty?


A:

<code>lst</code> is not empty, it contains one element, an empty string.
<code>print()</code> however prints the string representation of the object, and the string representation of an empty string is the empty string.
To print the contents of <code>lst</code>, use <code>print(lst)</code> instead.

