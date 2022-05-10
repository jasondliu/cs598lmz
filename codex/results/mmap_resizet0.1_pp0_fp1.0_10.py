import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I thought that the mmap would be able to read the data that was there before the truncate.
Is there a way to do this?


A:

<blockquote>
<p>I thought that the mmap would be able to read the data that was there before the truncate.</p>
</blockquote>
No, it won't.
<blockquote>
<p>Is there a way to do this?</p>
</blockquote>
No, there isn't.

