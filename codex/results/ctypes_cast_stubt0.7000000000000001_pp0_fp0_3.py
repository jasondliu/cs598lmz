import ctypes
ctypes.cast(0)
</code>
And I get this warning:
<code>python -qq libc.so.6
/usr/lib64/python2.7/ctypes/__init__.py:366: RuntimeWarning: "python -qq libc.so.6" found in cache, but
  hash mismatch
  return f(*args)
</code>
I don't quite know how to interpret this.


A:

The library is being loaded by ctypes but the dynamic linker finds a different version during the import. This can be seen by looking at the output of the <code>LD_DEBUG=libs</code> environment variable:
<code>$ LD_DEBUG=libs python -c 'import ctypes; ctypes.cdll.LoadLibrary("libc.so.6")'
[...]
        12803:     find library=libc.so.6 [0]; searching
        12803:      search cache=/etc/ld.so.cache
        12803:       trying file=/lib64/libc.so.6
        12803:
        12803:     find library=libc
