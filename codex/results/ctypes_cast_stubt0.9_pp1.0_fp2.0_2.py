import ctypes
ctypes.cast(arraytype, ctypes.POINTER(wintypes.HWND))
</code>
The following doesn't work either:
<code>ctypes.cast(arraytype, wintypes.HWND)
</code>
How do I correctly type the variables?


A:

Here is a short example of casting an array type of long:
<code># -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:55:42 2016

@author: Han
"""
import ctypes


if __name__ == '__main__':
    num = 5
    size = num*ctypes.sizeof(ctypes.c_long)
    ctype_long_array = ctypes.POINTER(ctypes.c_long)
    _array = (ctypes.c_long*num)()
    _array = ctypes.cast(ctypes.pointer(_array), ctype_long_array)

    _array[0] = 5
    _array[1] = 1
    _array[2] = 9
    _array[3
