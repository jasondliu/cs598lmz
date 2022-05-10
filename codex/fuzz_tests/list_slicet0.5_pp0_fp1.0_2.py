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
keepali0e.append(lst)
del keepali0e
print 'ok'
</code>
the output is:
<code>ok
</code>
And if you change the <code>while lst:keepali0e.append(lst[:])</code> to <code>while lst:keepali0e.append(lst[0])</code>, it will print <code>ok</code> and then raise <code>RuntimeError: deallocated C++ object</code>
So I think that the <code>while lst:keepali0e.append(lst[:])</code> will create a new list, so the original <code>lst</code> will not be deleted. But the <code>while lst:keepali0e.append(lst[0])</code> will not create a new list, so the original <code>lst</code> will be deleted.
Is my understanding correct?


A:

Your understanding is correct.
The first case creates a new list, and the second case doesn't.
<code>&gt;
