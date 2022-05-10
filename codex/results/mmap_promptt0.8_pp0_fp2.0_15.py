import mmap
# Test mmap.mmap() on a file that was just created.
with open('myfile', 'w+') as f:
    mm = mmap.mmap(f.fileno(), 0)
    mm.write(b'hello world')
    mm.seek(0)
    assert mm.read() == b'hello world'
    mm.close()
# Test mmap.mmap() on a file that was previously created.
with open('myfile', 'r+') as f:
    mm = mmap.mmap(f.fileno(), 0)
    assert mm.read() == b'hello world'
    mm.seek(0)
    assert mm.read() == b'hello world'
    mm.close()
