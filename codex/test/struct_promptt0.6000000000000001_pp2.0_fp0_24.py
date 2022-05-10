import _struct
# Test _struct.Struct.format_size
for t in ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd', 'P']:
    print("%c: %d" % (t, _struct.Struct(t).format_size("")))
# Test _struct.Struct.__sizeof__
