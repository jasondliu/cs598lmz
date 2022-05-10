import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
If you run this with Python 2.7, you get a <code>ValueError</code> exception:
<code>ValueError: mmap length is greater than file size
</code>
However, if you run it with Python 3.5, you get a <code>TypeError</code> exception:
<code>TypeError: slice indices must be integers or None or have an __index__ method
</code>
I don't understand why the error message is different. Is it a bug or a feature?
The error message is the same in Python 3.4, but the error itself is different:
<code>ValueError: mmap offset is greater than file size
</code>
I'm not sure which behavior is correct.


A:

The <code>mmap()</code> documentation states the following:
<blockquote>
<p>If <code>&lt;code&gt;length&lt;/code&gt;</code> is larger than the current size of the file, the file is extended to contain <code>&lt;code&gt;length&lt;/code&gt;</
