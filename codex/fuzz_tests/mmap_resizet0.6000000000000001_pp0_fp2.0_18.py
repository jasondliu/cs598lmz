import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 5, in &lt;module&gt;
ValueError: mmap length is zero
</code>
I was under the impression that the <code>f.truncate()</code> would extend the mmap.  Do I need to close and re-open the mmap?  Is there a better way to do this?


A:

You can't extend the <code>mmap</code> object; you need to unmap it, extend the file, and then remap the file.
The <code>mmap</code> module is a wrapper around the <code>mmap</code> system call, which is a simple wrapper around the <code>mmap2</code> system call, which is a simple wrapper around the <code>mmap</code> system call. The <code>mmap</code> system call maps a file into memory, and it doesn't support extending the mapping without unmapping it first.

