import _struct

# struct.pack(): convert Python types to string to store in binary
a = _struct.pack('>i', 1000000)
# struct.unpack(): convert string to Python types
a = _struct.unpack('i', b'\x00\x00\x0f\x42')

a = _struct.pack('>i', 139768889)
# >>> a
# b'\x00\x00\x15\x15'

# 4 bytes unsigned integer
# 8 bytes double float
a = _struct.unpack('!if', b'\x00\x00\x15`\xc9\x9d\x9a\x89\x99\x99\x99\x19')
# >>> a
# (57, 139768889.66666669)

# """Calculate a TCP checksum
#
#     Internet checksum algorithm, see RFC1071
#     http://www.faqs.org/rfcs/rfc1071.html
# """
#
# import _struct
#
#
# def checksum(
