import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:1] = b'2'
    m[0:1] = b'3'
    m.close()
</code>
When I run the above, I get the following output:
<code>m[0:1] = b'2'
Traceback (most recent call last):
  File "so.py", line 10, in &lt;module&gt;
    m[0:1] = b'2'
ValueError: can't modify size of memory mapping
</code>
Why does this happen?
Note: it runs on Linux


A:

You are trying to expand the memory mapping by writing 2 bytes instead of 1 byte.
If you have a file with 1 byte and you use a memory map to access it, you get a memory area of 1 byte, not 2 bytes.
So <code>m[0:1]</code> is the whole memory area. If you write 2 bytes, you will have to expand the memory area. But you are not allowed to expand the memory mapping.
To achieve what you want, you have to create a new mapping with <code>mm
