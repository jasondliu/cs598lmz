import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
I can't figure out why the value of <code>a</code> is <code>b''</code> when I expect it to be <code>b'\x01'</code>.


A:

The docs say:
<blockquote>
<p>If the file is resized or otherwise modified in a way that affects the memory mapping, modifications are not guaranteed to be written through to the file.</p>
</blockquote>
So you're not guaranteed to see the bytes you wrote to the file through the <code>mmap</code> object.  The docs also say:
<blockquote>
<p>It is also possible to map an entire file into memory (using the entire length of the file as the length parameter to the constructor).</p>
</blockquote>
So, the <code>mmap</code> object is referencing the file as it was when you created it, not as it is now.  You can confirm this by adding a <code>print(m[:])</code> after the <code>m = mmap.mmap(f.fileno(),
