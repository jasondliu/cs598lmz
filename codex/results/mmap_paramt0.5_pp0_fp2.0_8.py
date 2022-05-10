import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = 2
    m.close()
</code>


A:

<code>m[0]</code> is a byte.  You are trying to overwrite it with an integer.  The problem is with <code>bytes(1)</code>.  This is not what you want.  You want to write a single byte to the file.  Use <code>f.write(bytes([1]))</code> instead.

