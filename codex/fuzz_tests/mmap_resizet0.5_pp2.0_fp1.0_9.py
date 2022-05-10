import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Output:
<code>b''
</code>
I expected <code>a</code> to be <code>b'\x01'</code>.
Is this a bug or am I doing something wrong?


A:

This is expected behavior. From the docs:
<blockquote>
<p>The mmap constructor creates a memory-mapped file. The file must be open for reading or writing. If the length is not given, it defaults to the current size of the file. <strong>If the file is extended, the extra data is <em>uninitialized</em>.</strong> If the file is reduced, the extra data is discarded.</p>
</blockquote>
This means that when you truncate the file, the extra data is not cleared, it's just left in an uninitialized state. The uninitialized data is still there, but it's not guaranteed to be anything in particular.

