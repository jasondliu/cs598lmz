import mmap
# Test mmap.mmap() with fileno() argument



def test(file):
    print('Test with direct file.')
    # write a string
    m = mmap.mmap(file.fileno(), 10)
    m[0:5] = b'hello'
    m[6:10] = b'there'
    m.seek(0)
    print('contents: %r' % m.read(10))
    m.close()
    for flag in range(0, 10):
        # test small mmap
        print('Test small map, flag = %d' % flag)
        m = mmap.mmap(file.fileno(), 100, access=flag)
        if len(m) != 100:
            raise RuntimeError('small mmap did not return the correct size')
        m.close()
        # test large mmap
        print('Test large map, flag = %d' % flag)
        m = mmap.mmap(file.fileno(), 2 ** 31, access=flag)
