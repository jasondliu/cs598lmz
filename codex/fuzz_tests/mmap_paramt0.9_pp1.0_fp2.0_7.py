import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ | mmap.PROT_WRITE)
    m[2]=5  # index out of bounds
</code>
This causes my Python interpreter to crash with:
<code>Fatal Python error: Segmentation fault

Current thread 0x00007f06f1e39700 (most recent call first):
  File "reader.py", line 11 in &lt;module&gt;
</code>
There's no error if I remove the write permission (see below) but I still can't write to the mmaped region.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    m[2]=5  # index out of bounds
</code>
How can I safely allow the extension module to write into the mmaped region?


A:

The answer is: Don't. This is impossible.
<code>mmap</code> does not have any provisions for extending the file out of band by the Python interpreter. No combination of parameters that
