import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)
</code>
I am using Python 3.6.8 on Windows 10.
The output is:
<code>['', '']
</code>
I would expect the output to be:
<code>['', '']
</code>


A:

The problem is that the <code>str</code> object is never garbage collected, because it is referenced by the <code>lst</code> list. You can see this by adding a <code>print(gc.get_referrers(lst))</code> to your code:
<code>['', '']
[{'__module__': '__main__', '__qualname__': 'A', 'c': &lt;weakref at 0x7f4e4c0e4e68; dead&gt;}]
</code>
This shows that the list is referenced by the <code>A</code> object, which is still alive.
The <code>A</code> object is still alive because the weak reference is not yet dead. The weak reference will only be dead when
