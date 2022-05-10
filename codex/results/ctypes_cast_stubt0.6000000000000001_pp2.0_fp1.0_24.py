import ctypes
ctypes.cast(device_handle, ctypes.c_void_p)
</code>
This returns:
<code>&lt;__main__.LP_c_void_p object at 0x7ffccb6d0990&gt;
</code>
I need to be able to convert this to an int, but I am getting errors when I try to cast it to an int.  Any ideas?


A:

You need to dereference the pointer:
<code>int_value = ctypes.cast(device_handle, ctypes.c_void_p).value
</code>

