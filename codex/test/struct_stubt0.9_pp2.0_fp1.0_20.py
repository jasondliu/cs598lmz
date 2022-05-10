from _struct import Struct
s = Struct.__new__(Struct)
#s.__setattr__("format","II")
s.format = "II"
s.size = 8

#s.mro
#s.pack
#s.unpack

# !! ATTENTION !!
# On Windows, the packed stream and unpacked stream is different due to byte order
# Thus, can only be used on Windows (not cross-platform)

# One can use the s.format directly in the new function to produce a Struct object
_s = Struct('Oh My God')

########################################################################################################################
# 'binascii' module contains functions to transform between binary data and ASCII string (representing hexadecimal digits
########################################################################################################################
import binascii
binascii.b2a_hex(b'\x00\x0F[\x80\x00')  # str of two-character; for Windows, byte order should be taken into consideration
binascii.hexlify(b'\x00\x0F[\x80\x00')
