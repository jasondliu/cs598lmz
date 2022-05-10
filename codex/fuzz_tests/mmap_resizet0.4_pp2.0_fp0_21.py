import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I'm getting an error
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
Why is that?


A:

When you truncate the file, the mmap object is no longer valid, as there is no longer any file data to map.
From the docs:
<blockquote>
<p>If the file on disk is resized by an external entity like a text editor, the size of the mmap object does not change. This can be used as a form of inter-process locking, or for persistence.</p>
</blockquote>

