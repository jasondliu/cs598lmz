import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
import gc
gc.collect()
</code>
The output of this program is :
<code>Error in atexit._run_exitfuncs:
Traceback (most recent call last):
  File "/usr/lib/python3.3/weakref.py", line 117, in __call__
    self.cb(*self.cb_args)
ValueError: weakly-referenced object no longer exists
</code>
I think it is because the weakref callback is called when the program starts to exit. This is possbily the reason why this error does not happen when you create a shell and run this code in it. In the shell, the program stops at the end, the <code>exitfunc</code> is called, and then you add a new weakref to the list.


A:

Yes, it is the <code>sys.exitfunc</code> that is doing this. It runs when the program exits; it is not a regular Python function but a special case called by the interpreter when the interpreter is shut down.
If you want to
