import ctypes
ctypes.cast(ctypes.c_void_p.from_buffer(ctypes.addressof(i)), ctypes.POINTER(ctypes.c_char*7)).contents.value
</code>
<blockquote>
<p>b'1\x00\x00\x00\x00\x00\x00'</p>
</blockquote>

Alternative
<code>import numpy
numpy.frombuffer(bytearray(i), dtype='int8')
</code>
<blockquote>
<p>array([ 49,   0,   0,   0,   0,   0,   0], dtype=int8)</p>
</blockquote>

