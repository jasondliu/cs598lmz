import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I am expecting to get an empty byte. However, I get the following error:
<code>Traceback (most recent call last):
  File "C:/Users/sams/PycharmProjects/untitled/test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: memory view cannot include memory beyond the end of the underlying file
</code>
I have also tried to truncate the file before opening the map, but I get the same error.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
</code>
What is the correct way to truncate a file and then read its contents from the map?


A:

It looks like the problem is that <code>mmap</code> can only deal with files whose size is a multiple of the page size.
<code>&
