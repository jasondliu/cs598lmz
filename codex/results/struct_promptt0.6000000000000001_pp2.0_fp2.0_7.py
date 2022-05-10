import _struct
# Test _struct.Struct.

# Make sure the struct module is available.
try:
    import struct
except ImportError:
    print("SKIP")
    raise SystemExit

# Exercise the range of sizes and formats.

for fmt in "?bBhHiIlLfd":
    for size in range(1, 10):
        s = _struct.Struct(fmt * size)
        print(s.format, s.size)
        print(s.pack(*range(size)))

        if fmt in "fd":
            # floats and doubles: only test pack once
            continue

        # check unpack
        print(s.unpack(s.pack(*range(size))))
        print(s.unpack_from(s.pack(*range(size))))

        if fmt in "bB":
            # bytes: only test unpack once
            continue

        # check pack_into
        b = bytearray(s.size * 2)
        s.pack_into(b, s.size, *range(size))
        print(b)
        print(s.unpack_from(b
