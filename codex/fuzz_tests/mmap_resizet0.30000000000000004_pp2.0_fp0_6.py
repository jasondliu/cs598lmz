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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I would expect <code>a</code> to be <code>b''</code>.
Is this a bug or am I missing something?


A:

You are missing that the <code>mmap</code> object is not updated when you truncate the file. The <code>mmap</code> object is a view into the file, and you just changed the size of the file.
The <code>mmap</code> object is still valid, but it is now a view into a file that is 0 bytes long.

