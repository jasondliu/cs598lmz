import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
gc.collect()
print lst
</code>
I want to know why the output is <code>['&lt;weakref at 0x7f6f1c0e2a98; to 'A' at 0x7f6f1c0e2a90&gt;']</code>
I think the output should be <code>[]</code>

