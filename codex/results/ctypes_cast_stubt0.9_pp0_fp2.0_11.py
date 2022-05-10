import ctypes
ctypes.cast(str, ctypes.POINTER(ctypes.c_char_p))
TypeError: Original list to cast must be a list
</code>
However, I can get it to work by <code>c_string</code> each string in the list.
<code>str = ['str1', 'str2', 'str3']
ctypes.cast(str, ctypes.POINTER(ctypes.c_char_p))
# &lt;ctypes.LP_c_char_Array_4 object at 0x0000000004104120&gt;
</code>
My question is why does the following pass the <code>TypeError</code>?
<code>array = [ctypes.c_char_p('one'), ctypes.c_char_p('two'), ctypes.c_char_p('three')]
ctypes.cast(array, ctypes.POINTER(ctypes.c_char_p))
# &lt;ctypes.LP_c_char_Array_4 object at 0x0000000004104120&gt;
</code>


A:

In
