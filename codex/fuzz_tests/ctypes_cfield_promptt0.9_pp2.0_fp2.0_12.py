import ctypes
# Test ctypes.CField
c_str = c_char_p((b'\0\0\0\0\0'))
print(c_str.value)

# <codecell>

# Test concatenation of byte arrays
parts = [c_char_p((b'\x01')),
         c_char_p((b'\x00\x00')),
         c_char_p((b'\x0c\x02\0\0')),
         c_char_p((b'\x00\x01', c_char_p((b'\x01\x02')))),
         c_char_p((b'\x12\x01'))]
arr = c_char_p((b''))
for p in parts:
    if isinstance(p, c_char_p) and hasattr(p, 'value'):
        p = p.value
    arr += p
print(arr.value)

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <code
