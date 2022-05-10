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
I understand that the file size is 0, but I thought that the mmap would be able to access the data that was there before the truncate.
Is there a way to do this?


A:

The problem is that the <code>mmap</code> object is tied to the file descriptor, not the file object.  So when you truncate the file, the <code>mmap</code> object is still tied to the old file descriptor, which is now invalid.
The solution is to close the file object and reopen it.  This will give you a new file descriptor, which will be valid.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    f.close()


