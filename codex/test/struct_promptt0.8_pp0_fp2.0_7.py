import _struct
# Test _struct.Struct and _struct.unpack at various struct sizes and alignments
def test_struct_align(size):
    print('Alignment test: size %d' % (size,))
    print('1234 5678  ABCD')
    for alignment in range(1, size + 1):
        print(format(alignment, '5d') + ' ', end='')
        fmt = '=%ds' % (size,)
        pack = struct.Struct(fmt)
        buf = pack.pack(b'x' * size)
        for x in range(0, size - alignment + 1):
            y = x + alignment
            fmt = '=%ds' % (y,)
            pack = struct.Struct(fmt)
            try:
                unpack = pack.unpack_from
                unpack(buf, 0)
                print(' ', end='')
            except struct.error:
                print('x', end='')

        print(' ' * (size - alignment + 1), end='')
