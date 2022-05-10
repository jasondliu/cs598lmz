import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
I get the error:
<code>Traceback (most recent call last):
  File "mmaptest.py", line 10, in &lt;module&gt;
    m[0] = b'\x00'
ValueError: readonly buffer
</code>
What is the cause of this?


A:

From the <code>mmap</code> docs:
<blockquote>
<p>By default, all modifications to a memory map are ignored until the <code>&lt;code&gt;mmap&lt;/code&gt;</code> object is flushed using the <code>&lt;code&gt;flush()&lt;/code&gt;</code> method. </p>
</blockquote>
The <code>flush()</code> method is not magic, it doesn't make your mmap writable. It just writes the changes back to the file. You can't make changes to a read-only mmap.

