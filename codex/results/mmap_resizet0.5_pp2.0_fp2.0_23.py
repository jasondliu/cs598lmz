import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
mmap.error: [Errno 22] Invalid argument
</code>
I'm running Python 3.5 on a 64-bit Linux machine.


A:

I think the problem is that you are trying to read from a file that no longer exists.
The <code>m</code> variable is a memory-mapped file object that contains a reference to the file you opened.  When you call <code>f.truncate()</code>, you are telling the operating system that the file is now empty.  So when you later try to read from the memory-mapped file object, the operating system can't find the file to read from.
You can see this if you try to write to the memory-mapped file object:
<code>m[:] = b'a'
</code>
You get the following error:
<code>Traceback (most recent call last):
  File "test.py
