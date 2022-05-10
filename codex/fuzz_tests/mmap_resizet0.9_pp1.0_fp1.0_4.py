import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code throws the exception:
<code>Traceback (most recent call last):
  File "mmap_try1.py", line 18, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
When I look at the filesize for <code>test</code> it is <code>1</code>. So why does it throw an error?


A:

The underlying mmap library calls the Unix <code>mmap</code> system call to create the mapping.  Once the mapping is created, you are free to resize the file, but the original length is the length that the mapping sees, and if you shrink the file below the original requested length, you will get buffer overruns, segmentation faults, etc.

