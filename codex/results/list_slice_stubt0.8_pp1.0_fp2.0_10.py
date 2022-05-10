import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepalive=keepali0e
keepalive.append(a)
keepalive.append(a.b)
keepalive.append(a.c)
w=weakref.ref(a,callback)
del a
del keepali0e
print(lst)
del lst
</code>
The list doesn't get cleared.


A:

The problem is your <code>keepalive</code> list.
In the example, <code>keepalive</code> is used to keep a reference around to <code>a</code>. After <code>del lst[0]</code> executes, <code>keepalive[0]</code> still has a reference to <code>a</code>, which means that <code>a</code> isn't garbage collected, so <code>lst</code> isn't cleared.
You can fix this by removing <code>keepalive[0]</code> from <code>keepalive</code> after you remove the reference from <code>lst[0]</code>:
<code
