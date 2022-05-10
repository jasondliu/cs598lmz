import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In this case, I get <code>ValueError: memory view cannot include a terminator</code>
Looking through the code, the reason seems to be that this only returns <code>0</code>:
<code>f.seek(0, os.SEEK_END)
end = f.tell()
</code>
The docs say to me that<code>tell()</code> will return <code>0</code>. It does this for files opened in "w", "a" or "a+" modes. The only mode it does not do this for is "w+". It seems rather inconsistent that <code>tell()</code> behaves differently depending on the mode.
Is this a bug, or am I misunderstanding the docs/intended behaviour?
(Windows 7, Python 3.7.1)


A:

Just read the documentation:
<blockquote>
<p>You may not resize a file while it is being mmap’d.
  (On Windows, the file handle used by the mmap object must be obtained from the same file object that was used to create the mapping, and it must not have
