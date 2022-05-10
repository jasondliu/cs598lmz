import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I understand that the file is truncated, but I don't understand why the mmap object is not updated.
I'm using Python 3.6.4 on Windows 10.


A:

The documentation for <code>mmap</code> says:
<blockquote>
<p>The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> function may need to extend the file size. The <code>&lt;code&gt;access&lt;/code&gt;</code> argument specifies the desired access: <code>&lt;code&gt;PROT_READ&lt;/code&gt;</code> to read only, <code>&lt;code&gt;PROT_WRITE&lt;/code&gt;</code> to write only
