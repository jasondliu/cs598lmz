import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(sys.getsizeof(m))
    m.close()
</code>
<blockquote>
<p>128</p>
</blockquote>
<code>with open('test', 'r+b') as f:
    print(sys.getsizeof(f))
</code>
<blockquote>
<p>56</p>
</blockquote>
If you don't want to open the file in read+write mode, you can do this (it will be slower):
<code>with open('test', 'rb') as f:
    with open('test', 'r+b') as f2:
        m = mmap.mmap(f2.fileno(), 0, access=mmap.ACCESS_READ)
        print(m.read())
        m.close()
</code>

