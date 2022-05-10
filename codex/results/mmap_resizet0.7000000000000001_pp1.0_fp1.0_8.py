import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line results in:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: memory block deleted
</code>
Similarly, if the file is opened for text, the result is:
<code>ValueError: cannot resize file to smaller size
</code>
This seems like a bug, but maybe there is a reason for this.  I plan to work around it by using <code>mmap.resize()</code> before using <code>file.truncate()</code>, but it would be nice if it would just work.
This was tested with Python 3.4.3 on Linux.


A:

The documentation for <code>mmap</code> states:
<blockquote>
<p>When designing an application which will use mmap(), it’s important to remember that the <strong>underlying file will be modified by any changes made to the mmap’d region</strong>. Changes made by other <strong>processes</strong> to the underlying file
