import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
</code>
(I can also provide the code in C, if that is preferred.)
The problem is that after the callback is called, since I've already called <code>del lst[0]</code> the index is invalid (it's the internal C index, not Python index).
I've tried making the <code>list</code> a tuple, but that doesn't work either.  My next thought would be to add a <code>list</code> to the object and store the reference in the <code>list</code>.  But that is ugly.  I'd like to keep the reference in the list (or make it a tuple), but somehow make it so that the callback works. 
Perhaps I need to use another type of object (not a <code>list</code> or <code>tuple</code>).
Suggestions?


A:

If you really want to use the index, you have to have <code>lst</code> as a list, and you have to that that doesn't get garbage collected. This is pretty easy if <code>lst</code> is a global (or
