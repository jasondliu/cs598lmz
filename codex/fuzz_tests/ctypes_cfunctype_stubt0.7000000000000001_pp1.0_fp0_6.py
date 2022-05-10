import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

fun()
</code>
I get this error:
<code>---------------------------------------------------------------------------
Exception                                 Traceback (most recent call last)
&lt;ipython-input-8-6d9b6f2d9c8b&gt; in &lt;module&gt;()
      2 FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
      3 @FUNTYPE
----&gt; 4 def fun():
      5     return 0
      6 

&lt;decorator-gen-1&gt; in fun()

AttributeError: 'function' object has no attribute '_decorated'
</code>
I'm running Python 2.7.6 with IPython 2.1.0 on OSX 10.9.2.
How do I fix this?


A:

The <code>ctypes.CFUNCTYPE</code> factory function creates a type instance, not a decorator.  The <code>CFUNCTYPE</code> factory returns an instance of a type that subclasses the builtin <code>function</
