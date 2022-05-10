import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(lst[0],callback))
keepali0e.append(weakref.ref(a,callback))
del a

assert(lst==[])
</code>
But now I want to call <code>callback</code> on <code>lst[0]</code> and <code>a</code> when <code>lst</code> is empty. I've tried the following:
<code>class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(lst[0],callback))
keepali0e.append(weakref.ref(a,callback))
del a

while lst:
    pass
assert(lst==[])
</code>
But this causes an infinite loop. Why? 


A:

I think the <code>del lst[0]</code> in your callback is causing the <code>lst</code> to continue to be nonempty.  So
