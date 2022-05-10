import mmap
# Test mmap.mmap(-1, 2)

f = mmap.mmap(-1, 2)
f.write(b'ab')
f.seek(0)
if f.read(2) != b'ab':
    print('mmap failed to read file contents')
f.close()

f = mmap.mmap(-1, 2)
f[:] = b'ab'
f.seek(0)
if f.read(2) != b'ab':
    print('mmap failed to read file contents')
f.close()

f = mmap.mmap(-1, 2)
f.write_byte(b'a')
f.seek(0)
if f.read_byte() != b'a':
    print('mmap failed to read file contents')
f.close()

f = mmap.mmap(-1, 2)
f.write_byte(b'a')
f.seek(0)
if f.read(2) != b'a\x00':
    print('mmap failed to read file contents')
f.close()
