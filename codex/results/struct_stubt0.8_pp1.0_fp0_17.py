from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size   = struct.calcsize(s.format)
testdata = [
    (1, '\x00\x00\x00\x01'),
    (65536, '\x00\x01\x00\x00'),
    (65537, '\x00\x01\x00\x01'),
    (0xffffff, '\xff\xff\xff\xff'),
    (0xffffff + 1, '\x00\x00\x00\x00'),
    (sys.maxint, '\x7f\xff\xff\xff'),
    (sys.maxint + 1, '\x00\x00\x00\x00'),
]

for (value, bytes) in testdata:
    result = s.pack(value)
    if result != bytes:
        print 'error: expected', repr(bytes), 'got', repr(result)
        break
    else:
        print value, repr(result)
    value_ = s.unpack(bytes)[0]

