import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte
    y = ctypes.c_short
    z = ctypes.c_char

s = S(b'\x01', b'\x02\x03', b'\x04')
print s
</code>
prints
<code>Traceback (most recent call last):
  File "./x.py", line 9, in &lt;module&gt;
    s = S(b'\x01', b'\x02\x03', b'\x04')
TypeError: 'ubyte' object cannot be interpreted as an index
</code>
How to create the S object?  Of course I can use <code>S(1, 258, 4)</code>, but I don't want to hardcode the numbers since there's an ambiguity in the number of bytes in the source data for the x (1 byte), y (2 bytes) and z (1 byte) fields.
I thought maybe I could use <code>s = S(struct.unpack('BBB', b'\x01\x02\x03\x04')</code>
