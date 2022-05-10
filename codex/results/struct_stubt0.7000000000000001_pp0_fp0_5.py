from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'Ii4s'
data = "0x12345678"
print s.unpack_from(data)
</code>
This is the error message I got:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
struct.error: unpack requires a string argument of length 4
</code>
I am guessing the "0x" part is the cause, how should I unpack it? Thanks.


A:

First of all, you need to convert the hex string to a string of bytes.  For example:
<code>data = data.decode("hex")
</code>
Or, you can use <code>binascii</code> to do the same thing:
<code>import binascii
data = binascii.unhexlify(data)
</code>

However, this is still not going to work, because <code>struct.unpack_from</code> requires a buffer of binary data to unpack from.  In
