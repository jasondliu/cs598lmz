import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I have read the documentation and I understand that the <code>mmap</code> object is not aware of the changes to the file size. However, I don't understand why the <code>m[:]</code> line raises an exception. The documentation says that the <code>mmap</code> object can be used as a sequence, and I would expect the <code>m[:]</code> line to return an empty sequence.
Is there a way to get an empty sequence without raising an exception?

