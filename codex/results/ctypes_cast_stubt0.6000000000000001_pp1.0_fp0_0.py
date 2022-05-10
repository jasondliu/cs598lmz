import ctypes
ctypes.cast(struct.pack("!I", 0x01020304), ctypes.c_char_p).value
# '\x04\x03\x02\x01'
</code>

