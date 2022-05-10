import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works fine on Linux, but on Windows it raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that this is because the file is truncated before the <code>mmap</code> is created, but I don't understand why it works on Linux.
I've tried to find the answer in the documentation, but I couldn't find anything.
Is there a way to make it work on Windows?


A:

The documentation for <code>mmap</code> says:
<blockquote>
<p>If <code>&lt;code&gt;length&lt;/code&gt;</code> is larger than the current size of the file, the file is extended to contain <code>&lt;code&gt;length&lt;/code&gt;</code> bytes.</p>
</blockquote>
So the file is extended to contain 1 byte, and then you can read it.
On Windows, the file is truncated to 0 bytes before the <code>mmap</code> is created, so the file is empty.

