import ctypes
ctypes.cast(matrix, ctypes.c_void_p)
</code>
But this doesn't work. I get the error:
<blockquote>
<p>TypeError: expected LP_c_char instance instead of LP_c_int instance</p>
</blockquote>
I have also tried to use <code>ctypes.addressof</code>:
<code>ctypes.addressof(matrix)
</code>
But this doesn't work either. I get the error:
<blockquote>
<p>TypeError: 'int' object is not callable</p>
</blockquote>
I am not sure how to get the address of the matrix in memory. How can I get the address of the matrix in memory?


A:

<code>addressof</code> is a function, not a method. So you need to call it like this:
<code>ctypes.addressof(matrix)
</code>
<code>addressof</code> returns a value, it doesn't modify the object.

