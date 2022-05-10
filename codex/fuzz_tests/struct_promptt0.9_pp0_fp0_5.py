import _struct
# Test _struct.Struct by encoding a few disparate types.
print _struct.Struct.__doc__

for code, value in [('c', 65), ('d', 0.25)]:
    print _struct.Struct(code).pack(value)

for code, value in [('=c', 65), ('=d', 0.25)]:
    print _struct.Struct(code).pack(value)

for code, value, bigendian in [('c', 65, False), ('d', 0.25, True)]:
    print _struct.Struct(code).pack(value, bigendian)

for code, value in [('f', 0.0), ('f', 1.0), ('f', -1.0), ('f', float('nan')), ('f', float('inf')), ('f', float('-inf')),
        ('d', 0.0), ('d', 1.0), ('d', -1.0), ('d', float('nan')), ('d', float('inf')), ('d', float('-inf')),
        ]:
    print _struct.Struct('<' + code
