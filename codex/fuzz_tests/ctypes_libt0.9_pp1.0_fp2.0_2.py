import ctypes
ctypes.CDLL("libm.so.6",mode=ctypes.RTLD_GLOBAL)
ctypes.CDLL("libquadmath.so.0",mode=ctypes.RTLD_GLOBAL)
</code>
This only works really if you are using python3.4.  Introduce a line
<code>import ctypes
ctypes.CDLL("libm.so.6",mode=ctypes.RTLD_GLOBAL)
</code>
in the file <code>math.cpython-34m-x86_64-linux-gnu.so</code> (you may have to modify the path).
The second line is only necessary if you want to use <code>ComplexWarning</code>.

