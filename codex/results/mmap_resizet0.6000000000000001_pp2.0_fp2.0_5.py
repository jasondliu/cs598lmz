import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect <code>len(a) == 0</code>, but it's <code>1</code>.
How can I get an empty byte string?


A:

<blockquote>
<p>How can I get an empty byte string?</p>
</blockquote>
<code>m[:]</code> is the memory-mapped file. If you truncate the file, you truncate the memory-mapped file, too. It's the same file.
<code>a = m[:]</code> copies the data from the memory-mapped file to <code>a</code>. Truncating the file doesn't affect <code>a</code> any more than truncating the file affects the data in the file itself.
If you want <code>a</code> to be an empty byte string, don't copy the data from the memory-mapped file.
<code>a = bytes()
</code>

