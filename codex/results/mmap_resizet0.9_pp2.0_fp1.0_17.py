import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The error happens at the line where <code>a</code> is assigned. I understand this is because the file is truncated and hence the length of the slice we requested is not possible any more.
My question is: Is there any way to be sure that <code>a</code> has been assigned correctly - i.e. without any exceptions? If we replace <code>m[:]</code> by <code>m[0]</code> or <code>m[0:1]</code> there is no exception but then the value of <code>a</code> might not be what we expect.


A:

This is a bug in the python 3 implementation of <code>mmap</code>. It tries to access the file even after <code>FlushViewOfFile</code> has been called. 
We can fix our bug by explicitly telling <code>mmap</code> that the file size is different:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r
