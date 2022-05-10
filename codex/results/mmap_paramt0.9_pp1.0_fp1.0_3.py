import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(3) # &lt;--- ValueError: Assignment must be same size as slice
</code>
The solution seems to be setting <code>f.seek(0, 2)</code> in this case. What about larger files and keeping the size?


A:

There is a bug with <code>mmap</code> on Windows that causes a <code>ValueError</code> if the file size changes. This bug is fixed in Python 3.7, but the proposed patch is not included in the distro version.
According to this comment in the bpo, <code>tempfile.TemporaryFile</code> fixes the problem because it "expands the file".
The exception is much more detailed in Python 3.7:
<blockquote>
<p>File "D:\Python\36\lib\mmap.py", line 252, in resize_</p>
<pre><code>&lt;code&gt;  self._get_win_size() * self._setting_size)
&lt;/code&gt;</code></pre>
<p>ValueError: embedded null
