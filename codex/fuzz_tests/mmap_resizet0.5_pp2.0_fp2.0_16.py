import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I'm trying to get the contents of a file, then truncate it and get the contents again.  I'm using the mmap module to get the contents of the file.  I'm getting the error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
I tried to flush the mmap object, but that didn't seem to help.  Is there a way to do this?


A:

You can't mmap an empty file.  You can't even mmap a file that has a length of 0.
If you want to truncate the file, you have to close the mmap first.

