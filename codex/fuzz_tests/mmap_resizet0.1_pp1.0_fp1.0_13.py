import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I would expect the <code>mmap</code> to be updated with the new file size.
I'm using Python 3.6.5 on Windows 10.


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The size argument specifies the initial size of the mmap’s data. The optional access argument specifies the access policy of the mmap. It defaults to <code>&lt;code&gt;ACCESS_DEFAULT&lt;/code&gt;</code> (allowing read and write access).</p>
</blockquote>
So, you need to specify the size of the file when you create the <code>mmap</code> object.
<code>m = mmap.mmap(f.fileno(), 1)

