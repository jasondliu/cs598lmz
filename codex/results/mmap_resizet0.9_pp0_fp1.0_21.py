import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The code raise the following exception:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 12, in &lt;module&gt;
    a = m[:]
ValueError: memory must be accessible
</code>
But I expected that in "a" i will get "bytes(1)" (1), but the file is already empty.
I am right expecting that code should work or it is not allowed?


A:

You are not allowed to truncate the file that is currently being mmaped, because it invalidates the memory map.
As the docs say:
<blockquote>
<p>If length is zero, the entire file is mapped (the default). <strong>If length is nonzero, the mmap contains length bytes starting with offset offset.</strong></p>
</blockquote>

