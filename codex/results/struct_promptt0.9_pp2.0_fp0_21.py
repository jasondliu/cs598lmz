import _struct
# Test _struct.Struct
def pack_unpack(buf, fmt):
    print buf.encode('hex')
    packed = s.pack(fmt, buf)
    print packed.encode('hex')
    unpacked = s.unpack(fmt, packed)
    print unpacked[0].encode('hex')
    print (buf == unpacked[0])

s = _struct.Struct("<H")
pack_unpack("\xff\xff", "<H")
pack_unpack("\xff\x77", "<H")
s = _struct.Struct("<BBBBBBBBBBBBBBB")
pack_unpack("\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff", "<BBBBBBBBBBBBBBB")
pack_unpack("\xff\x77\xff\x77\xff\x77\xff\x77\x77\x77\xff\xff\xff\xff\xff", "<BBBBBBBBBBBBBBB")

print _struct.calcsize("@")
print
