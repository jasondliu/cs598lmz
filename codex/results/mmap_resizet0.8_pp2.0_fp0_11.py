import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises:
<blockquote>
<p>File "", line 1, in </p>
<p>OSError: [Errno 22] Invalid argument</p>
</blockquote>
Why? How can I make it work?


A:

First, truncating a file is almost certain to change the file size, which means all memory maps based on it are invalid. See the <code>mmap()</code> documentation:
<blockquote>
<p>Modifying a file through a mmap() object will modify the original file. </p>
</blockquote>
You can use <code>mmap.resize()</code> to adjust the memory map to the new size, if it has not changed.
If the file is empty and you are using Windows, you also need to call <code>fileobj.flush()</code> first:
<blockquote>
<p>For example, if <em>fileobj</em> is a file opened with <code>&lt;code&gt;os.open()&lt;/code&gt;</code> in Windows,
