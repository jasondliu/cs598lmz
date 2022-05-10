import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line throws <code>ValueError: mmap closed or invalid</code>.
I'm using Python 3.4.3 on Windows 7.
I know that I can use <code>mmap.resize</code> to resize the file, but I want to know why the above code doesn't work.


A:

The <code>mmap</code> object is a view of the file, and when you truncate the file, the view is no longer valid.
From the <code>mmap</code> documentation:
<blockquote>
<p>The <code>&lt;code&gt;mmap&lt;/code&gt;</code> module defines the following exception:</p>
<p><code>&lt;code&gt;mmap.error&lt;/code&gt;</code></p>
<p>This exception is raised on any error. It is a subclass of <code>&lt;code&gt;OSError&lt;/code&gt;</code>.</p>
</blockquote>
and
<blockquote
