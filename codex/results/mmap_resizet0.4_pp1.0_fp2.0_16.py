import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I would have expected <code>a</code> to be <code>bytes(0)</code>.
Is there a way to get this behavior?


A:

The problem is that you are using the <code>mmap</code> object after the underlying file has been truncated. This is undefined behavior:
<blockquote>
<p>If a file is resized (e.g., with <code>&lt;code&gt;truncate()&lt;/code&gt;</code> or <code>&lt;code&gt;ftruncate()&lt;/code&gt;</code>), any
  mappings of the entire file are invalidated, and any attempt to access
  the resized portion of the file will generate a <code>&lt;code&gt;SIGBUS&lt;/code&gt;</code> signal.</p>
</blockquote>
The <code>mmap</code> object is not aware that the file has been truncated, so
