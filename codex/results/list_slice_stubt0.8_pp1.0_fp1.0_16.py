import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
a.b=lst
del a
del lst
gc.collect()
gc.callbacks.append(callback)
time.sleep(2)
print len(callback.__self__.callbacks)
</code>
Output:
<code>On Windows, the output is 0
On Linux, the output is 1
</code>
Why callback by <code>gc.callbacks</code> is not called on Windows?
The two operating systems above are both 64-bit Windows and 64-bit Linux.


A:

I found the answer with the help of python's issue tracker.
The reason for this problem is that w_weakref_destroy does not call w_weakref_callback in Windows.
The code is in the <code>Modules/gcmodule.c</code> file:
<code>#ifdef MS_WINDOWS
    Py_DECREF(ref-&gt;wr_callback);
#else
    w_weakref_callback(ref);
#endif
</code>

