import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

@jit(nopython=True)
def f():
    return fun()

print(f())
</code>
Gives the following error:
<code>TypingError: No implementation of function Function(&lt;function fun at 0x0000020D8D831AE8&gt;) found for signature:
  (object, ) -&gt; object
</code>
I was unable to find any documentation on how to do this.


A:

If you are using Python 3.7, you are probably using Numba 0.41 or newer.
The <code>@jit</code> decorator has been deprecated in favor of <code>@njit</code> (or <code>@jit(nopython=True)</code>)

