import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Will a be non-empty?


A:

No, <code>a</code> will be empty (<code>b''</code> to be exact). The <code>read()</code> operation will fail upon an attempt to read more than the number of bytes currently available in the file, i.e. 0.
<blockquote>
<p>Description:</p>
<p>The <strong>mmap</strong> function returns a mmap object for the specified file <em>(which is either an absolute or relative file name)</em> or file descriptor <em>(if specified as an integer)</em>.</p>
<p>If <em>length</em> is <code>&lt;code&gt;0&lt;/code&gt;</code>, the maximum length of the map is the current size of the file when <code>&lt;code&gt;mmap&lt;/code&gt;</code> is called.</p>
</blockquote>

