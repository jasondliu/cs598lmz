import _struct
# Test _struct.Struct.
for fmt in "bBhHiIlLfd":
    try:
        s = _struct.Struct(fmt)
    except TypeError:
        print(fmt, "not supported")
    else:
        print(fmt, s.size)
        print(s.pack(1))
        print(s.unpack(s.pack(1)))

print('{:d} {:d} {:d}'.format(1, 2, 3))
print('{:d} {:d} {:d}'.format(1, 2))
print('{:d} {:d} {:d}'.format(1, 2, 3, 4))
print('{:d}'.format())
print('{:d}'.format(1, 2))
print('{:d} {:d} {:d}'.format(1, 2))
print('{:d} {:d} {:d}'.format(1, 2, 3, 4))
