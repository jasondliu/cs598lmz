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
I tried to analyze it, but I failed. What is this script doing, and what is the point of these <code>keepalive</code> references?


A:

My findings so far:
It crashes on this line:
<code>while lst:keepali0e.append(lst[:])
</code>
Why? List slicing creates another object that refers to the original object, thus preventing the gc from deleting it. There is no reference to list <code>lst</code> anywhere else, so when <code>lst</code> is deleted, there is nothing left that refers to it.
It crashes on this line because it tries to delete the weakref in <code>keepali0e</code> that refers to <code>a</code>. When this happened, there was no reference left to the list the weakref was in, so the weakref callback was the last thing to refer to the list. However, <code>keepali0e</code> continues to refer to the same list, which is already deleted.
We can see this in the following example:
<code>&gt;&
