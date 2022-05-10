import _struct
# Test _struct.Struct class with non-native size
import string

for format in ['<HHl', '>HHl', 'BHI', 'BHI']:
    hh_l = _struct.Struct(format)
    for data in (b'\x01\x01\x00\x00\x00\x01',
                 b'\x01\x02\x00\x00\x00\x02',
                 b'\x01\x03\x00\x00\x00\x03',
                 b'\x01\x04\x00\x00\x00\x04'):
        s = hh_l.unpack(data)
        p = hh_l.pack(s[0], s[1], s[2])
        if p != data:
            print("%s != %s" % (string.hexify(p), string.hexify(data)))
            print("format %s, unpacked %s, repacked %s" % (hh_l, s, p))
            print("error: expected %s, got %s\
