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
The line <code>lst=[str()]</code> ensures that<code>lst</code> contains a single item that cannot cause any further action when it is collected. If <code>lst</code> goes in to an infinite loop because it references it self, it is <code>a</code> that maintains a reference to <code>lst</code>. By removing the first element from <code>lst</code> we can get <code>lst</code> to be collected. Then the outer loop will terminate (or rather the inner loop breaks).
Note that the program will terminate whether <code>lst</code> is made to loop or not.

