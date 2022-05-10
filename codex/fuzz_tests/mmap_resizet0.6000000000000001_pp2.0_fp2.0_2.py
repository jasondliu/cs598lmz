import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line produces the following error:
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    a = m[:]
ValueError: mmap slice assignment is wrong size
</code>
Does anyone know how to fix this? This is a simplified example of the issue I am having with a larger program.


A:

I think you need to close the mmap object first, then truncate the file.

