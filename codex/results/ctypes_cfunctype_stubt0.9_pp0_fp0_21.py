import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return y
globals()['fun{}'.format(11)] = fun

print(fun, fun.__code__.co_code)

import dis; dis.dis(fun)

%time fun()
</code>
gives
<code>&lt;function fun at 0x11e96bd90&gt; b'k\x00\x00j\x01\x00j\x01\x00d\x00S'
  1           0 LOAD_GLOBAL              0 (y)
              3 RETURN_VALUE        

1.35 µs ± 5.24 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
</code>
Which shows that if I want to call the function inside another function, I can do
<code>def runner():
    return globals()['fun{}'.format(11)]()
</code>
and
<code>def runner():
    return eval('fun{}'.format(11))()
</code>
However, this only calls the function.  Is there a way to determine the
