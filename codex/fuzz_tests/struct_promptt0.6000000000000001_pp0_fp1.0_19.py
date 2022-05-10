import _struct
# Test _struct.Struct with the struct module's formats.
for code in struct.__dict__:
    if code[0] == '_' or code == 'pack' or code == 'unpack':
        continue
    fmt = struct.__dict__[code]
    print code, fmt, _struct.calcsize(fmt)
    assert _struct.calcsize(fmt) == struct.calcsize(fmt)
    a = _struct.Struct(fmt)
    assert a.format == fmt
    assert a.size == struct.calcsize(fmt)
    b = struct.Struct(fmt)
    assert a.pack(*(b.unpack(a.pack(*range(a.size/struct.calcsize('i')))))) == a.pack(*range(a.size/struct.calcsize('i')))
    assert a.pack_into(*(b.unpack(a.pack(*range(a.size/struct.calcsize('i')))) + (0,))) == a.pack(*range(a.size/struct.calcsize('i')))

