import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
</code>
After executing this code, <code>test</code> has length 2.
However, if I change the <code>m.resize(2)</code> line to <code>m.resize(4)</code>, <code>test</code> does not get resized. Why?


A:

You have to open the file in read-write mode, as the documentation says:
<blockquote>
<p>When opening a file in binary mode (i.e. <code>&lt;code&gt;'b'&lt;/code&gt;</code> is appended to the mode argument), you must supply the size argument otherwise the file size is determined using <code>&lt;code&gt;fstat&lt;/code&gt;</code>.</p>
</blockquote>
This is the code I am using to test this:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f
