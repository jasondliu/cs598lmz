import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]='a'
del a
del keepali0e
print lst
</code>
The output is <code>['a']</code> and not <code>[]</code> as I expected.
I tried to find a solution in this question, but it's not what I want.
I want to delete the element from the list, not just set it to <code>None</code>.


A:

You can use the <code>weakref.finalize</code> class to achieve this.
<code>import weakref

def callback(x):
    del lst[0]

lst = [str()]
a = A()
a.c = a
finalizer = weakref.finalize(a, callback)
lst[0] = 'a'
del a
del keepali0e
print lst
</code>

