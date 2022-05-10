import mmap
# Test mmap.mmap for writing
def test_mmap():

    try:
        f = open('test.bin', 'w')
    except:
        return ret

    f.write('\x00' * mmap.PAGESIZE)
    f.close()

    try:
        f = open('test.bin', 'r+')
    except:
        return ret

    try:
        m = mmap.mmap(f.fileno(), mmap.PAGESIZE, access=mmap.ACCESS_WRITE)
        m[0] = '\xff'
        m.close()
        f.close()
        ret = 1
    except mmap.error:
        f.close()

    os.remove('test.bin')
    return ret

