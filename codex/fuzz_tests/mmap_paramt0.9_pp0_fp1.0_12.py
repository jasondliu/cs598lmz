import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
</code>
It won't change the content of the file.
I could use
<code>f.write(m)
m.close()
</code>
But in my real code, I store the file pointer, so the last <code>m.close()</code> is not performed. Will it create a memory leak?
if no, then why can't I use <code>m[0] = b'\x01'</code> to change the content directly?


A:

Just call <code>flush()</code>:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.flush()
</code>

