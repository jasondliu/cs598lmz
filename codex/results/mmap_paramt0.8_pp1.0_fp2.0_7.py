import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
    m.seek(0)
    m.write(bytes(2))
    m.close()
</code>
I got output:
<code>b'\x00'
</code>
The first byte is <code>\x00</code>. It is not <code>\x01</code>. How could <code>r+</code> mode return <code>\x00</code>?
I cannot understand the document. (https://docs.python.org/3.7/library/mmap.html#mmap.mmap)
<blockquote>
<p>mmap.mmap(fileno, length, access=ACCESS_DEFAULT, flags=MAP_SHARED, prot=PROT_WRITE | PROT_READ, offset=0)</p>
<p>The access flags determine whether it is possible to read from, write to, or execute the new buffer. The default value depends on the flags and the operating system, and is read-only on most systems. On systems where the default is read-write, specifying ACCESS_READ as
