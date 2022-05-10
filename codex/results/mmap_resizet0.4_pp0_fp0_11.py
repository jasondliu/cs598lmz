import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This gives me the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
How can I do this?


A:

The problem is that you're trying to map a file that's 0 bytes long.  If you truncate the file after creating the mapping, the mapping will still be valid, but it will be empty.
If you want to truncate the file and then read from the mapping, you'll need to create a new mapping to the new size of the file.

