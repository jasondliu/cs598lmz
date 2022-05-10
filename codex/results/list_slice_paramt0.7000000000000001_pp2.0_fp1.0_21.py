import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
import gc
gc.collect()
</code>
When <code>__del__</code> method is called, I can't use <code>self</code> because <code>self</code> is already unavailable. So, I want to remove this <code>self</code> from <code>lst</code>. In this case, I will not be able to use <code>self</code> in <code>callback</code> function. So, I tried to keep a reference to <code>self</code>. But, it didn't work for me. Here, I tried to keep a reference to <code>self</code> in <code>keepali0e</code>. But, <code>gc.collect()</code> deleted <code>self</code> from <code>keepali0e</code> too. So, <code>callback</code> function couldn't remove the object from <code>lst</code>. How can I do this?
