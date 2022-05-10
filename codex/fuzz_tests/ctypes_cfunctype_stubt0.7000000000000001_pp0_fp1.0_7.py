import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
a = fun()
print a
</code>
It works, but I'm worried about the GIL:
<blockquote>
<p>The GIL is released to allow other Python threads to run while the
  callback is running, but interrupts are disabled, so the callback is
  unable to trigger a signal handler. This is done to prevent the
  callback from executing arbitrary Python code while the C code is
  holding the lock, which could otherwise lead to a deadlock.</p>
</blockquote>
I have no idea what an "interrupt" is. How can I release the GIL while keeping "interrupts" enabled?
(I don't care about deadlocks. I'm implementing a pure-Python JIT compiler, no Python code will be called from within my "interrupt", and I want my "interrupt" to be able to call Python code.)


A:

<blockquote>
<p>I have no idea what an "interrupt" is.</p>
</blockquote>
You should read about signals.  They are asynchronous events that can be triggered from the outside to notify things like "Ctrl-C
