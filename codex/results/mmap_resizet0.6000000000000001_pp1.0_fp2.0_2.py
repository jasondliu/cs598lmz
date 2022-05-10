import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expect the output to be <code>b'\x00'</code>, but it's <code>b'\x01'</code>.
Why?
If I remove <code>f.truncate()</code>, the output is <code>b'\x01'</code> as expected.


A:

<code>mmap</code> objects are not updated when the underlying file is truncated.  They refer to the original file data.
If you want to use a <code>mmap</code> object with a truncated file, you need to reopen it after truncating the file.

