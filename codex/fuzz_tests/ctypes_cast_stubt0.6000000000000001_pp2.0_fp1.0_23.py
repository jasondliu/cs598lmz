import ctypes
ctypes.cast(ctypes.pointer(sock.send_data), ctypes.POINTER(ctypes.c_char))
</code>
But I get an error:
<blockquote>
<p>TypeError: expected LP_c_char, got LP_c_ubyte</p>
</blockquote>
I'm not sure what to do next. Any ideas?


A:

I finally figured out a solution that works for me.
<code>import ctypes
buffer = (ctypes.c_ubyte * 4096)()
buffer[:] = sock.send_data[:]
ctypes.cast(buffer, ctypes.POINTER(ctypes.c_char))
</code>

