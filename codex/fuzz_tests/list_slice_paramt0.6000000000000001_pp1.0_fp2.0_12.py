import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:print lst
</code>
In python 2.7, it prints <code>['&lt;ref at 0x7f1d1a0c0ae8; dead&gt;']</code> and then <code>[]</code>. 
But in python 3.3, it prints <code>['&lt;ref at 0x7f1d1a0c0ae8; dead&gt;']</code> and then <code>['&lt;ref at 0x7f1d1a0c0ae8; dead&gt;']</code> and then <code>[]</code>. 
So, in python 3.3, the weakref callback is called twice. 
I am using python 3.3 and I want the weakref callback to be called only once. 
I know the solution to this problem is to not use <code>del lst[0]</code> in the callback, but use <code>lst.pop(0)</code> instead.
But I am looking for a solution that does not require me to change the code.
