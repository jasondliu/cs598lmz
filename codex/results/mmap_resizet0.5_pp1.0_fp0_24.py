import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get <code>mmap.error: [Errno 22] Invalid argument</code> on the last line.
If I change <code>f.truncate()</code> to <code>m.resize(0)</code>, everything works. Why is that?


A:

<code>m.resize(0)</code> is the right way to go if you want to truncate a file and keep the memory map.
You can't truncate the file and keep the memory map because the file is now shorter than the memory map.  If you truncate the file, the memory map will be invalidated.
The <code>mmap</code> module documentation says:
<blockquote>
<p>If the file is resized or otherwise modified in a way that would make the memory map invalid, the <code>&lt;code&gt;mmap&lt;/code&gt;</code> object must be re-initialized.</p>
</blockquote>

