import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This prints b'\x00' on my machine.  This is an implementation detail of the Python interpreter, but it should be safe to open the file with <code>'r+b'</code> and then <code>'w+b'</code> (and probably safe to open it <code>'rb'</code> and then <code>'wb'</code>).
<code>mmap</code> is a very thin wrapper around <code>mmap()</code> from the C standard library, and the Python documentation says:
<blockquote>
<p>The file object must stay alive until the <code>&lt;code&gt;mmap&lt;/code&gt;</code> object is closed or discarded (which makes it impossible to use <code>&lt;code&gt;mmap&lt;/code&gt;</code> in a <code>&lt;code&gt;with&lt;/code&gt;</code> statement), otherwise Python will crash with a fatal error (invalid memory access).</p>
</blockquote>
so, while it is valid
