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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
Why does this happen? I thought that the <code>mmap</code> object would be updated when the file is truncated.


A:

<blockquote>
<p>I thought that the mmap object would be updated when the file is truncated.</p>
</blockquote>
No, it won't.
<blockquote>
<p>Why does this happen?</p>
</blockquote>
Because the file is truncated, and the <code>mmap</code> object is still pointing to the old file.
<blockquote>
<p>I thought that the mmap object would be updated when the file is truncated.</p>
</blockquote>
No, it won't.
<blockquote>
<p>Why does this happen?</p>
</blockquote
