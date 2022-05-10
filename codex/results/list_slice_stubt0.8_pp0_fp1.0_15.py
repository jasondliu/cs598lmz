import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(weakref.ref(lst,callback))
del a
del lst
gc.collect()
</code>
The problem with this approach is that it makes the <code>lst</code> object keep a reference to <code>a</code>, which may not be desirable---if, for example, you only care about the <code>c</code> attribute of the object. The other problem is that, as I discovered when testing this, it doesn't actually work. The thing is, once you put the <code>str()</code> at the head of the list, it stays there, even when you're trying to remove it, because whenever you try to remove it, the list gets reallocated, and the COW mechanism comes into play and makes it effectively immutable.
Solution #3: <code>delattr</code>
If you just want the <code>c</code> attribute to be deleted along with the object, you can probably use <code>delattr</code> to get the behavior you want:
<code>class B(object): pass
b = B()
b
