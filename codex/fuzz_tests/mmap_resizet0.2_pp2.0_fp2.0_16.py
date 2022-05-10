import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I understand that this is because the file has been truncated, but I don't understand why. I thought that the <code>mmap</code> object would have a reference to the file descriptor, and therefore the file would not be truncated until the <code>mmap</code> object was closed.
I also tried this code:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close()
    a = m[:]
    print(a)
</code>
This code throws an exception:
<code>Traceback (most recent call last):

