import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
print lst
</code>
The output is <code>['', '']</code>, but I expected <code>[]</code>.
Why does this happen?


A:

The problem is that you are using a <code>weakref</code> to the object <code>a</code> and a <code>weakref</code> to the attribute <code>a.c</code>. 
When you delete <code>a</code>, the <code>weakref</code> to <code>a</code> is called, but the <code>weakref</code> to <code>a.c</code> is not called. 
The <code>weakref</code> to <code>a.c</code> is only called when you delete <code>a.c</code>. 

