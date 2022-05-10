import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
</code>
So, lst has one item and <code>keepalive</code> has one weakref pointing <code>a.c</code>. Setting to None is handled specially if the weakref contains the cyclic garbage. At that point, the weakref points to None and its callback is called. The weakref's callback <code>del lst[0]</code>.
Now, at this point, the object <code>str()</code> is in <code>lst</code> and it also has a refcount <code>2</code>. <code>2</code> because the weakref points to an object that has a reference to the <code>str()</code> object. Python has no way to know that that str() object is the only remaining object. Python can't assume that there won't be another object containing a reference to it. So it doesn't get deleted. 
However, if you have <code>lst=[13]</code>, deleting the weakref deletes the only remaining reference to the <code>int</code> object 13 and it gets deleted.
This is explained in the docs.

