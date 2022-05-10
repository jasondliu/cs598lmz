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
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I'm not sure why this is happening. I'm guessing that the mmap is not being updated when the file is truncated. Is there a way to fix this?


A:

<code>mmap</code> is not a general-purpose file wrapper.  It's a wrapper around a specific region of a file.  When you truncate the file, the region of the file that the <code>mmap</code> is wrapping is gone.  You can't access it.  You can't even re-<code>mmap</code> it.
If you want to truncate a file, you should close the <code>mmap</code> first.

