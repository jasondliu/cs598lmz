import ctypes
ctypes.cast(a, ctypes.c_int32)
&gt;&gt;&gt; &lt;ctypes.c_int32_Array_4 object at 0x7f835a6adbe0&gt;
</code>
But I cannot do this in cython because as soon as I cast, I lose the array:
<code>cdef c_int *a
ctypes.cast(a, ctypes.c_int32)
&gt;&gt;&gt; &lt;ctypes.c_int32 object at 0x7f835a6adb30&gt;
</code>
I have tried to use the cython memoryview to get the address of the array, but again I seem to get a single element:
<code>cdef c_int *a
b = c_int32[4](1,2,3,4)
cdef int[:] c = &lt;int[4]&gt; b
c_int.from_address(&lt;char*&gt;c.data)
&gt;&gt;&gt; &lt;ct
