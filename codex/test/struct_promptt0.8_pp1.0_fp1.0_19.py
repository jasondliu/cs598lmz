import _struct
# Test _struct.Struct.

with _struct.Struct('iif') as t:
    s = t.new_buffer(24)
    print(t.format, t.size, t.alignment, file=sys.stderr)

    t.pack_into(s, 0, 1, 2, 3.0)
    print(s.tobytes(), file=sys.stderr)

    t.pack_into(s, 8, 4, 5, 6.0)
    print(s.tobytes(), file=sys.stderr)

    t.pack_into(s, 16, 7, 8, 9.0)
    print(s.tobytes(), file=sys.stderr)

    x = t.unpack_from(s, 8)
    print(x, repr(x), x.__class__, file=sys.stderr)
    # Note that the tuple is not a subclass of 'tuple'.
    assert x.__class__ is tuple

