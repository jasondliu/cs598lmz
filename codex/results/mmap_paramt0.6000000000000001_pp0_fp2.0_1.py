import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\0')
    m.seek(0)
    m.write(b'\1')
    m.flush()

with open('test', 'rb') as f:
    print(f.read())

</code>
This prints <code>b'\x01'</code> as expected. On Linux, this is fine. On Windows, however, if I try to read the file before the <code>with</code> block ends, I will get the original value <code>b'\x00'</code>. The file is only updated after the <code>with</code> block ends.
I have tried using <code>f.truncate()</code>, <code>f.flush()</code>, and <code>m.flush()</code> to no avail.
Any ideas?


A:

I believe I found the answer.
The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>Windows: If length is 0, the maximum length of the map is the current size of the file. The file
