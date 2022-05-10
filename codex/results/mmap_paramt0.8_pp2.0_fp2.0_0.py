import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(5))
    m.close()


with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(len(m))
    print(m[1])
    m.close()
</code>
<code>len(m)</code> prints <code>6</code>, but I would expect <code>5</code> instead, because the file is only <code>5</code> bytes long. Is it supposed to be like this?


A:

Yes, it's supposed to be like this. The spec says this about <code>mmap</code>'s <code>size</code> argument:
<blockquote>
<p>The optional <em>size</em> argument specifies the size of the buffer used to represent the mapping. Its default value is the current size of the file when mode includes <code>&lt;code&gt;mmap.MAP_SHARED&lt;/code&gt;</code>; otherwise, its default value is zero.</p>
</blockquote
