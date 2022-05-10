import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I would expect that the <code>mmap</code> object would be updated to reflect the new file size.
Is there a way to make this work?


A:

The <code>mmap</code> object is not updated to reflect the new file size.
The <code>mmap</code> object is a view of the file at a particular point in time.  If the file is changed, the <code>mmap</code> object is not updated.
You can use <code>mmap.resize</code> to resize the <code>mmap</code> object.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno
