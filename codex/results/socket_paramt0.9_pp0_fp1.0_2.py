import socket
socket.if_indextoname(bytearray(b'\x00\x12\x34\x56\x78\x90'))
</code>
You can also use <code>bytearray.tobytes()</code> instead of <code>bytes(bytearray)</code>.

