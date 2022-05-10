import mmap
# Test mmap.mmap(0,1).close() -- Trigger a bug in some builds (Issue 5202)
with mmap.mmap(0, 10) as m:
    assert m.read(4) == b"\0\0\0\0"
    m.write(b'abcd')
    m.seek(0)
    assert m.read(4) == b'abcd'
    m.close()
    m.close()
    m.close()
    raises(TypeError, m.seek, 0)
    raises(TypeError, m.read, 1)
    raises(TypeError, m.write, b'e')
    raises(TypeError, m.flush)

with mmap.mmap(-1, 0) as m:
    raises(ValueError, m.write_byte, 'a')
    raises(ValueError, m.write, b'a')
