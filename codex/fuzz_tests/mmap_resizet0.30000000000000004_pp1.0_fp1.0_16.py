import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code>.
I would expect that the output would be <code>b'\x01'</code> since the file was truncated after the mmap was created.
I'm using Python 3.6.4 on Windows 10.


A:

<code>mmap</code> is not a file object. It is a memory-mapped file object.
You can't truncate a file that is memory-mapped. You can't truncate a file that is open. You can't truncate a file that is open for reading. You can't truncate a file that is open for writing. You can't truncate a file that is open for reading and writing.
You can truncate a file that is open for writing, but only if you opened it with <code>O_TRUNC</code>.

