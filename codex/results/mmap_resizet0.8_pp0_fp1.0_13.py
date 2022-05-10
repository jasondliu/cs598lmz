import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In the last line, I get a <code>ValueError</code> exception. Changing <code>m[:]</code> to <code>m[:1]</code> does not raise any exception. Why does this happen?


A:

The error is happening because the <code>mmap</code> has no data.
You are truncating the file to zero bytes, so the map is now invalid, as it maps a file that is now smaller than the mapped region. Attempting to read from a map that is no longer valid raises the exception, as seen in the source:
<code>if len(data) != length:
    raise ValueError("mmap length is inaccurate")
</code>
You can check if a map is valid with the <code>closed()</code> method:
<code>&gt;&gt;&gt; m.closed()
False
&gt;&gt;&gt; f.truncate()
&gt;&gt;&gt; m.closed()
True
</code>

