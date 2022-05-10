import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code fails with <code>ValueError</code> exception on the last line. <code>m[:]</code> seems to produce the exception.
I understand that this happens because the write mode mapping is not consistent with the truncation of the file. But I am confused. Does the documentation say something about this? I thought <code>r+</code> mode means the file could be read and written.  
How could I modify the above code so that it works?

