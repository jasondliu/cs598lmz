import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 48
    m.close()
</code>
Now if I check the file with <code>hexdump</code>, it has the expected value (30)
<code>00000000  30 0a                                             |0.|
</code>
However, if I use <code>file.read()</code> I get the old value (31).
Is there something I misunderstand?


A:

The problem is that you are opening the file in read-only mode (<code>r</code>) so python is caching the file contents in memory before returning a file object to you.  When you <code>m[xxx] = yyy</code>, you are writing through the underlying file descriptor and reading directly from disk when you <code>m.read()</code>.  If you instead open the file in read-write mode <code>r+</code>, you'll get the expected behavior.  This is because when the file is opened in read-write mode, the file contents are neither cached nor synchronized with the file data; i.e., read/write operations on the file object's buffer and the file data are independent
