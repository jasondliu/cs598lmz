import ctypes
ctypes.cast(hDisplay, ctypes.c_void_p).value
<Sdkdll.HANDLE object at 0x0000000000F4CD30>
int(ctypes.cast(hDisplay, ctypes.c_void_p).value)
3456787
</code>

