import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
It outputs <code>b'\x01'</code> and <code>test</code> file is empty.
I expected <code>a</code> to be <code>b''</code> and <code>test</code> file to contain <code>b'\x01'</code>.
Why is it so and how can I achieve my expected behavior?


A:

This is the expected behavior.
From the docs:
<blockquote>
<p>The mmap object is a window on a file. It is not a copy of the file,
  and changes to the mmap object are reflected in the file.</p>
</blockquote>
So when you truncate the file, the mmap object is also truncated.

