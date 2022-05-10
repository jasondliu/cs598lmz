import _struct
import _sys

# The following is an example of how to use this class.
# 
# >>> import _struct
# >>> format = _struct.Struct("<i")
# >>> buf = format.pack(42)
# >>> buf
# '*\x00\x00\x00'
# >>> format.unpack(buf)
# (42,)
# >>> buf = format.pack(-42)
# >>> format.unpack(buf)
# (-42,)
# >>> buf = format.pack(2**31 - 1)
# >>> format.unpack(buf)
# (2147483647,)
# >>> buf = format.pack(2**31)
# >>> format.unpack(buf)
# (2147483648,)
# >>> buf = format.pack(2**31 + 1)
# >>> format.unpack(buf)
# (2147483649,)
# >>> buf = format.pack(-2**31)
# >>> format.unpack(buf)
# (-2147483648,)
# >>> buf = format.pack(-2**31
