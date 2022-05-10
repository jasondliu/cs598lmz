import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
print lst
del keepali0e 
print lst
</code>
I would like to have a list that only has <code>str()</code> in it.
I was told to use <code>weakref.ref</code> and <code>del</code> to achieve the goal.
However, I don't understand why this code can't work?
Here I want to say <code>keepali0e</code> is a list that only contains one item, and that item is a weak reference to <code>a.c</code>.
And when I delete <code>keepali0e</code>, the item in <code>keepali0e</code> will be deleted, and <code>callback</code> will be called.
But when I run this code, the <code>lst</code> still contains <code>str()</code>.
What's the problem?
I think the reason is that I don't understand what <code>weakref</code> means.
I know the <code>weakref</code> can be collected by <code>gc</
