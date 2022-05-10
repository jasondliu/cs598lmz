import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Traceback:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
Why is this? Why is mmap giving me this error? I'm not even trying to use the mmap object, I'm just trying to access it. I'm not sure what the proper way to handle this is.


A:

When you truncate the file, the mapping becomes invalid.  You need to remap it.

