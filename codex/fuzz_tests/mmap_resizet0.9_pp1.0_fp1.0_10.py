import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
print(len(a))
</code>
The output of this is:
<code>b''
0
</code>
It seems that <code>mmap(..., 0)</code> re-mapps the file when it shrinks. Is this the expected behavior? I would like to be able to keep writing to the same mmap'd location even if the file gets truncated.


A:

A memory map (especially to a file) is only as long as the source file, and when the source file is truncated it immediately reflects this change by becoming those same number of bytes (from the start of the file). If you truncate a 10 byte file down to 6 bytes and then try to get the final four bytes out of the memory map, you'll get a <code>ValueError</code> out of the <code>read()</code> operation as you have attempted to read past the end of the file.
The <code>fileno</code> method returns an int representing the file descriptor of the underlying file object.
The <code>mmap</code> with the size of file you have there is equivalent to <code
