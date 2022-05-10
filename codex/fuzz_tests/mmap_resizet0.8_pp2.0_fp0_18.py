import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The problem is that m[:] doesn't raise OSError. The mmap is stored in m, but m[:] doesn't actually raise an OSError. Is there any way to prevent the mmap from reading old data when the file changes?


A:

This is probably a bug in mmap.  It looks like the slice accessor is just returning a slice of the bytestring rather than accessing the original file.  This is not really a bug in the sense that nobody should ever rely on a mmap object that is no longer valid.
You could write your own accessor that checks the size of the file and raises an exception if the size is different:
<code>def m_slice(m):
    if m.size() != os.stat(m.filename).st_size:
        raise IOError('File size changed')
    return m[:]
</code>

