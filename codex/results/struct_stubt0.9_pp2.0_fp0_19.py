from _struct import Struct
s = Struct.__new__(Struct)
s.format = ">xI"
buf = "\x00spam\x00"
print buf
print s.unpack(buf)
# print s.unpack_from(buf)

print "\n#$" * 40 

print unpack(">xI", "\x00spam\x00")
