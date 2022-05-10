import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm not sure why this is happening. I'm using Python 3.6.5.


A:

The problem is that you are truncating the file after you have created the memory map.
The memory map is created with the size of the file at the time it is created.
If you truncate the file after creating the memory map, the memory map will still be the size of the file at the time it was created.
If you truncate the file before creating the memory map, the memory map will be the size of the file at the time it was created.
If you want to truncate the file after creating the memory map, you will need to resize the memory map.

