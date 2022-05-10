import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
a.l=weakref.ref(b,callback)
lst.append(b)
del b
lst.append(A())
del lst[1:]
lst.append(A())
print len(keepalive)
</code>


A:

I think Python deletes the objects in <code>keepalive</code> (in the order they appear in the list) at the time that the <code>del</code> statement is executed. To test this hypothesis, I added the following code immediately after the <code>del</code> statement and it printed the number of objects in <code>keepalive</code> as <code>0</code> (as expected):
<code>print len(keepalive)
</code>

