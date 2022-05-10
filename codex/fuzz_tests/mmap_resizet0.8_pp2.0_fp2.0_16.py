import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
print(a)

with open('test', 'rb') as f:
    a = f.read()
print(a)
</code>
It prints:
<blockquote>
<p>b'\x01'<br/>
  b''</p>
</blockquote>
It seems that the buffer of <code>mmap</code> still holds old data. I want to use <code>mmap</code> to read and write large files quickly. But I cannot use <code>truncate</code> anymore. How can I solve this problem? Preferably without reading the whole file into memory and writing it back, because that process is very slow.


A:

<blockquote>
<p>How can I solve this problem? Preferably without reading the whole file into memory and writing it back, because that process is very slow.</p>
</blockquote>
That, in fact, is all the kernel is doing.  From <code>man 2 truncate</code> ...
<blockquote>
<p>truncate() causes the regular file named by path or
