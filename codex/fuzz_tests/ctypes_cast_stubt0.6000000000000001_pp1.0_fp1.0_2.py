import ctypes
ctypes.cast(lib.get_version, ctypes.CFUNCTYPE(None))
</code>
This fails, with the following error:
<blockquote>
<p>ValueError: CFUNCTYPE() argument 1 must be callable</p>
</blockquote>
I have tried casting it to <code>ctypes.CFUNCTYPE(None, ctypes.c_int)</code> and <code>ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_int))</code>, both with the same result.
What is the correct way to cast the function pointer to a callable?


A:

You can't cast the function pointer to a callable. You must define a callback function that accepts an <code>int*</code> argument and then pass that to <code>CFUNCTYPE</code>:
<code>#define get_version get_version_

void get_version(int* version);

void get_version(int* version) {
    *version = 1;
}
</code>
<code>import ctypes


