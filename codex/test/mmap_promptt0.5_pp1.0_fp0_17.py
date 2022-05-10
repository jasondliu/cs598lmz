import mmap
# Test mmap.mmap.read

with open(TESTFN, 'wb') as f:
    f.write(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09')

with open(TESTFN, 'rb') as f:
    m = mmap.mmap(f.fileno(), 10, access=mmap.ACCESS_READ)
    assert m[0] == 0
    assert m[1] == 1
    assert m[-1] == 9
    assert m[-2] == 8
    assert m[0:9] == b'\x00\x01\x02\x03\x04\x05\x06\x07\x08'
    assert m[1:9] == b'\x01\x02\x03\x04\x05\x06\x07\x08'
