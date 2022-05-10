import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code runs fine and produces the expected result, but with a warning:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
Is there a better way to do this without getting the warning?


A:

The error you get is not a warning, it is a raised exception.
The reason you are getting this exception is that you are using <code>mmap.mmap()</code> with <code>size=0</code> (as <code>0</code> is the default). This is invalid because you are trying to create a mapping of an empty file.
From the documentation:
<blockquote>
<p>If <code>&lt;code&gt;size&lt;/code&gt;</code> is 0, the maximum length of the map will be the current size of the file when mmap is called.</p>
</blockquote>
You already truncate your file before creating the <code>mmap
