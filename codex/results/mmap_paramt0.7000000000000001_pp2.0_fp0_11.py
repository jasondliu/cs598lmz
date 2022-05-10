import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(1024)
    f.seek(1024)
    f.write(bytes(1))
</code>
Output:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 7, in &lt;module&gt;
ValueError: can't resize memory map that is accessed directly or whose file cannot be resized
</code>
I've tried <code>m.flush()</code> after <code>m.resize()</code> and I get the same error.
Using Python 3.2.3, <code>Linux 3.2.0-23-generic #36-Ubuntu SMP Tue Apr 10 20:39:51 UTC 2012 x86_64 x86_64 x86_64 GNU/Linux</code>.
Any ideas?
EDIT:
The reason I want to do this is that I was thinking it would be faster to write to a pre-allocated <code>mmap</code> file than to use a <code>io.StringIO</code> (which is what I'm using now).

