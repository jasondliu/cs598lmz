import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code will raise an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I thought that <code>mmap</code> will be updated after <code>truncate</code> call.
Is it possible to update <code>mmap</code> after <code>truncate</code> call?


A:

You can't use <code>mmap</code> on a file that has been truncated to zero length.  The <code>mmap</code> module is a wrapper around the <code>mmap</code> system call, which is documented as:
<blockquote>
<p>The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> system call causes the pages starting at <code>&lt;code&gt;addr&lt;/code&gt;</code> and continuing for at least <code>&lt;code&gt
