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
Why does it not cause a RecursionError?


A:

The important bit of your question is 
<blockquote>
<p>while lst:keepali0e.append(lst[:])</p>
</blockquote>
If you remove that line, the code will recurse.
This is because when you do <code>keepali0e.append(lst[:])</code>, you are creating a copy of the list - when you add the list to the <code>keepalive</code> list, you're not adding the list itself, but a copy of the list. As a result, the <code>del lst[0]</code> will succeed, and the list will be empty.
When you remove this line, the <code>while</code> loop will run indefinitely, and use up 100% of your CPU.

