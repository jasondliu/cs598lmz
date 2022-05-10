import mmap
# Test mmap.mmap() with size=0
with mmap.mmap(-1, 0) as m:
    print('mmap(0) with len = ' + str(len(m)))
    print('mmap(0) with tell = ' + str(m.tell()))
    m[0] = b'a'
    m.seek(2**16)
    m.write(b'a')
    print('mmap(0) with len = ' + str(len(m)))
    print('mmap(0) with tell = ' + str(m.tell()))
    try:
        m[2**16] = b'b'
    except IndexError:
        print('exception as expected: mmap(0)')
# Test mmap.mmap() with size=1
with mmap.mmap(-1, 1) as m:
    m.write(b'a')
    print('mmap(1) with len = ' + str(len(m)))
    print('mmap(1) with tell = ' + str(m.tell()))
    m[0
