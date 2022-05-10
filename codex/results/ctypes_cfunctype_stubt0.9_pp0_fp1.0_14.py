import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hi"
</code>
results in
<code>ValueError: Function found with wrong signature: fun().
</code>
With <code>rtld_flags=ctypes.RTLD_NOW | ctypes.RTLD_GLOBAL</code> the import worked, i.e.,
<code>dl = mercurial.dynamic.LIBRARY()
dl.sym('fun', ctypes.py_object, ctypes.py_object, rtld_flags=ctypes.RTLD_NOW | ctypes.RTLD_GLOBAL)
</code>
The first argument <code>ctypes.py_object</code> is the return type. The <code>py_object</code> is a pointer, so if I would want <code>const char *</code> as the return type it ought to be <code>ctypes.c_char_p</code>, right? The second argument <code>ctypes.py_object</code> is not <code>const char *</code> because the original hg_extension_utils.c declares the signature with <code>void</
