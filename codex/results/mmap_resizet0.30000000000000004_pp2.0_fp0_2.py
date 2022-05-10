import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I want to read the content of the file before truncating it. But the above code raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I can't understand why the <code>mmap</code> object is not updated after the <code>truncate</code> call.
Is there a way to read the content of the file before truncating it?


A:

<code>mmap</code> is a memory-mapped view of the file.  It doesn't know about the file size.  It's just a view of the memory.  It doesn't know about the file at all.  It doesn't know about the file size.  It doesn't know about the file contents.  It doesn't know about the file name.  It doesn't know about the file system.  It doesn't know about the operating system.  It doesn't know about the hardware.  It doesn't know about the universe. 
