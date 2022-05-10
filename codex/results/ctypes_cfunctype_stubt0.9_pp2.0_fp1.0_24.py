import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return 3

fun.__name__ = "singlethreaded"
</code>
There are two problems with this approach: the first one is that I don't know how to declare a <code>@staticmethod</code> using Python's ctypes module API. The second problem is that the function gives an error when I try to serialize it:
<code>&gt;&gt;&gt; dumps(fun)
Traceback (most recent call last):
  File "/usr/lib/python2.7/cPickle.py", line 1382, in save_global
    klass = whichmodule(klass, name)
  File "/usr/lib/python2.7/cPickle.py", line 1352, in whichmodule
    raise ValueError, "could not find class %s" % name
ValueError: could not find class CFUNCTYPE_helpers.&lt;lambda&gt;

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt
