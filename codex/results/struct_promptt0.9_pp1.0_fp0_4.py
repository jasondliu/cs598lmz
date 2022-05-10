import _struct
# Test _struct.Struct().unpack_from() and .pack_into() with alignment.
p = _struct.pack_into

Aligned = _struct.Struct('h x 2l')
for align in (1, 2, 4, 8):
    for fmt in ['@', '=']:
        for data in [b'ab' b'cd' b'ef' b'gh', b'ab' b'cd' b'ef' b'gh' b'x']:
            for offset in range(len(data) + 2):
                uninit = data + b' ' * (align-1)
                u = uninit[offset:]
                unpack, pack = u[:Aligned.size], uninit[offset:]
                Aligned.pack_into(pack, 0, *range(1, 1 + len(Aligned.format)))
                result = Aligned.unpack_from(unpack, 0)
                expected = range(1, 1 + len(Aligned.format))
                equal = result == expected
                assert equal

# Test endian-ness.
ByteOrder = _struct.Struct('i
