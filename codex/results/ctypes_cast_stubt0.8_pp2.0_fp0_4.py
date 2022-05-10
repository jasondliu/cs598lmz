import ctypes
ctypes.cast(pointer.to_bytes(4, 'little'), ctypes.POINTER(ctypes.c_int)).contents.value == 5

</code>


A:

You need to pack the bytes into an integer before converting to a pointer. You can do this using <code>int.from_bytes</code> or <code>struct.unpack</code>:
<code>&gt;&gt;&gt; ctypes.cast(int.from_bytes(pointer.to_bytes(4, 'little'), 'little', signed=True), ctypes.POINTER(ctypes.c_int))[0]
5
&gt;&gt;&gt; ctypes.cast(struct.unpack('&lt;i', pointer.to_bytes(4, 'little')), ctypes.POINTER(ctypes.c_int))[0]
5
</code>
or more concisely:
<code>&gt;&gt;&gt; ctypes.cast(ctypes.c_int.from_buffer(pointer.to_bytes(4, 'little')), ctypes.POINTER(
