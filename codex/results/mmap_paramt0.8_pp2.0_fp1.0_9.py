import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)
    m[0] = b'1'
</code>
I receive the error: <code>TypeError: must be read-write buffer, not _mmap.mmap</code>. What am I doing wrong?


A:

There are two issues here:
1. The <code>bytes</code> object you're trying to write to the file is too short
This code:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))
</code>
Will write a single "zero" byte to the file. You probably meant this:
<code>with open('test', 'wb') as f:
    f.write(bytes([1]))
</code>
See here:
<code>&gt;&gt;&gt; bytes(1)
b'\x00'
&gt;&gt;&gt; bytes([1])
b'\x01'
</code>
2. You need to expand the map to 2 bytes
This:
<code>    m = mmap
