import ctypes
ctypes.cast(data, ctypes.c_void_p).value
</code>
But I am getting the error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: Byte objects are not supported as bitfields
</code>


A:

I'm not sure why you need the raw binary to be a pointer type so much but if you're willing to try something new, you may look at the <code>struct</code> module for this type of thing. This approach also supports endianness, and would probably make parsing the raw binary simpler since the module is made for exactly this purpose.
However, the <code>struct</code> module doesn't support bitfields, so one solution that may work is to pack the bytes into a number, and then dissect that number into the bit offsets that you need, something like this:
<code>import struct

raw = b'\xb1\x00\x18\x12'
data = struct.unpack('&gt;I', raw)[0]

length = (data &
