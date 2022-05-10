import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
b=A()
b.c=a
del a
keepalive.append(b)
weakref.ref(b,callback)
del b
lst
</code>
If:
<code>b.c=b
</code>
Then the list is empty.
Why the list is not empty in the first example?


A:

<blockquote>
<p>Why the list is not empty in the first example?</p>
</blockquote>
It is empty in the first example. What you are seeing is a memory-reuse "feature" of the Python interpreter; when the list is shrunk after garbage collection, the last entry is reused for the list's new length. Python list entries are stored in a continuous memory block.
To convince yourself, run your program in a Python debugger and set a breakpoint at the <code>lst[0]</code> line. You'll see that the list is empty and the <code>id()</code> value of <code>lst[0]</code> is the same as the <code>id()</code>
