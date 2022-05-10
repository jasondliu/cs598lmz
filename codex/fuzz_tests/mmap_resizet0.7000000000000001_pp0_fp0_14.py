import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # throws Exception
</code>
It throws an exception: 
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:] # throws Exception
ValueError: memoryview: underlying buffer has been detached
</code>
Is this expected behaviour?
If yes, is there a way to resize the underlying mmap to match the new underlying file size?
Edit:
I found the following code to work:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:] # this works now
</code>
I would like to know if this is the best way to do it, or if I can avoid using <code>resize</code>.


A:

<code>mmap</code> is the interface to memory-mapped files.  The purpose of mapping files into memory is to make the file contents accessible to user code as though the file contents were
