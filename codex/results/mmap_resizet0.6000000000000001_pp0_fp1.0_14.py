import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This results in an <code>mmap.error: [Errno 9] Bad file descriptor</code> at the line <code>a = m[:]</code>.
I'm using Python 3.4.3 on Windows 7.
Why does the error occur and how can I solve it?


A:

<blockquote>
<p>Why does the error occur?</p>
</blockquote>
The file descriptor that you passed to <code>mmap()</code> is no longer valid; it was closed when you <code>truncate()</code>d the file.
<blockquote>
<p>How can I solve it?</p>
</blockquote>
Don't <code>truncate()</code> the file.
Instead, use <code>mmap()</code> to write new data to the file.  For example, if you want to write a single byte, <code>0x42</code>, to the file, you can do this:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap
