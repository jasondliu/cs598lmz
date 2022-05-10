import mmap
# Test mmap.mmap()
def test_mmap():
    f = open('testfile.tmp', 'wb')
    f.write(bytes(x for x in range(0, 1000000)))
    f.close()
    f = open('testfile.tmp', 'rb')
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print('Test file is 1000000 bytes long')
    print('First 100 bytes via read :', m.read(100))
    print('First 100 bytes via slice:', m[:100])
    print('2nd   100 bytes via read :', m.read(100))
    print('2nd   100 bytes via slice:', m[100:200])
    m.close()
    f.close()
    try:
        os.unlink('testfile.tmp')
    except:
        pass

# Test mmap.mmap() with keyword arguments
def test_mmap_kwargs():
    # We do not check whether the arguments are actually used, but just
    # that they do not cause a Type
