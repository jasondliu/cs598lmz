import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_double)
f = FUNTYPE(lambda x: print("Calling f({})".format(x)))
f(1.0)
</code>
This will print "Calling f(1.0)".
From the documentation:
<blockquote>
<p>The CFUNCTYPE factory function is used to define C compatible
  callback types</p>
</blockquote>

