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
There is a cyclic reference between an <code>A</code> object and itself. Then <code>a</code> is discarded, and there is only one weak reference left. The callback is supposed to be called when only the weak reference left is cleared.
However, the interpreter crashes. The exact error message is:
<code>File "C:\Python27\lib\weakref.py", line 261, in _remove_dead_callback
    del self._all_weakrefs[wr]
KeyError: &lt;weakref at 0x00000000037A1128; to 'str' at 0x00000000037A1548&gt;
</code>
This means <code>a</code>'s weak reference is removed twice, but when? Probably when it is added to the list, but why?

