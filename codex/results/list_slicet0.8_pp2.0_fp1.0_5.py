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
    pass
</code>
I got the following output:
<code>['&lt;weakref at 0x02F84090; to 'A' at 0x02F84070&gt;']
</code>
I can understand that <code>A</code> object is alive, since it's reference is held by <code>a.c</code> and <code>c</code> is not a weakref.
But why does the <code>A</code> object appear in the <code>weakref</code> callback?
I expected to get no output at all.
EDIT: 
The real question is:
Why does the <code>A</code> object appear in the <code>weakref</code> callback when <code>A</code> is not really weakrefable (the circular reference)?
@Quentin: The answer lies in the <code>if</code> statement inside the <code>weakeref.py</code> file;
<code>if o is not None:
</code>
EDIT 2:
To clarify my question, I changed the code above to the following:
<code
