import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line gives me an error:
<code>Traceback (most recent call last):
  File "C:\Users\danny\Desktop\mmap.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
I would have expected it to return an empty array, but apparently mmap does not correctly handle empty files.
Is there a way to make this work?


A:

<blockquote>
<p>I would have expected it to return an empty array, but apparently mmap does not correctly handle empty files. Is there a way to make this work?</p>
</blockquote>
No.  The <code>mmap</code> module makes a mapping from the file to memory.  If the file is empty, there is nothing to map.  You can't map an empty file.

