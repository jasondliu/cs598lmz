import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # Error here
</code>
At line <code>a = m[:]</code> I am getting an error:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
Does the truncation somehow invalidate the mapping? How can I prevent this?


A:

Python VM is making the memory allocation and it can be much bigger than 0 bytes so when you truncate the file Python VM may not know it and use the memory which was already allocated by OS. 
According to the docs you should do <code>mmap.resize(new_size)</code> before truncating the file.

