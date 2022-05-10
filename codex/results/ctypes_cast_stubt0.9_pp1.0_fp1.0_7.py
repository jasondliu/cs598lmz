import ctypes
ctypes.cast(maptr, ctypes.POINTER(PIXELA))[0]  # Fails
ctypes.cast(maptr, ctypes.POINTER(PIXELA))[1752] # Fails
# &lt;class 'ctypes.pythonapi.PyObject_AsReadBuffer'&gt;", "&lt;-9&gt;"
</code>
However writing to the memory works:
<code>ctypes.cast(maptr, ctypes.POINTER(PIXELW))[0].r = 0xff
ctypes.cast(maptr, ctypes.POINTER(PIXELW))[0].g = 0xaa
ctypes.cast(maptr, ctypes.POINTER(PIXELW))[0].b = 0x55
ctypes.cast(maptr, ctypes.POINTER(PIXELW))[0].a = 0x00
bm.show()
</code>
Output of the above command:

Writing 0x0 as alpha affects the output. It is a visual confirmation that r, g and b values were written
