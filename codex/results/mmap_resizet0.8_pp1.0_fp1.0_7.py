import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Gives me the error <code>IndexError: memory mapped sequence is immutable</code> at the last line, but if the last line is <code>a = m[0]</code> then it doesn't.
The Python docs say:
<code>Changes in the file's size are reflected in the mmap object, so that
invoking mmap.size() will always return the size of the file, even if
it was later increased.
</code>
but it doesn't really say anything about changing the size of the file to be smaller than the mmap object.
How can I keep the memory map after the <code>truncate</code>?


A:

If you truncate the file, then the remaining length is not reflected in the mapping.
<code>  File "test.py", line 7, in &lt;module&gt;
    a = m[:]
IndexError: mmap slice assignment is larger than mmap size
</code>
Changing the last line to:
<code>a = m[0]
</code>
gives you a 1-byte string (the last byte
