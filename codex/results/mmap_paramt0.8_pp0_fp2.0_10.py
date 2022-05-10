import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'
    m.close()
</code>
I am getting the error: 
<code>Traceback (most recent call last):
  File "C:/Users/work/PycharmProjects/perf/test/__main__.py", line 10, in &lt;module&gt;
    m[0] = b'2'
TypeError: must be read-write buffer, not mmap
</code>
is there a way to make the mmap object a read-write buffer ?


A:

The documentation states:
<blockquote>
<p>This module is a wrapper around the system calls used for reading and writing...</p>
</blockquote>
It doesn't even attempt to provide any other functionality.
If you want to change the file itself, look at the <code>fileinput</code> module for editing files in place, or just read it into a string and then write it out again.

