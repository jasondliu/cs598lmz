import ctypes
ctypes.cast(config_update_ptr.value, ctypes.POINTER(ctypes.c_void_p))
</code>
compiler : VisualStudio 2013
python : 

version : 2.7.11 
64 bit



A:

Okay, I got it running:-)
In my source I have
<code>...
libfoo.config_update.argtypes = [ctypes.c_void_p]
...
</code>
but it should be
<code>...
libfoo.config_update.argtypes = [c_void_p_p]
...
</code>
after that, everything works.

