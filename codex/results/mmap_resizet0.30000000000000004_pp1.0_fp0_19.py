import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I don't understand why this happens. I thought that the <code>mmap</code> object would be updated when the file is truncated.
I'm using Python 3.6.1 on Windows 10.


A:

<blockquote>
<p>I thought that the mmap object would be updated when the file is truncated.</p>
</blockquote>
No, it's not.
<blockquote>
<p>I don't understand why this happens.</p>
</blockquote>
Because you truncated the file and the memory map is still pointing to the old file size.
<code>&gt;&gt;&gt; m = mmap.mmap(f.fileno(), 0)
&gt;&gt;&gt; f.truncate()
&gt;&gt;&gt; m.size()
1
</code>

