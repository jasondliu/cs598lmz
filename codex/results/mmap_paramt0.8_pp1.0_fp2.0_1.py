import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[:] = bytes(2)
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
I know I can write <code>bytes(2)</code> to <code>test</code> with <code>open('test', 'wb')</code>. But I want the <code>mmap</code> object to write <code>bytes(2)</code> to <code>test</code>.


A:

If you want to replace the bytes, you need a <code>mmap</code> that is as long as the bytes you want to replace. You get that length by calling <code>len()</code> on your <code>bytes</code> object:
<code>m = mmap.mmap(f.fileno(), len(bytes(2)), access=mmap.ACCESS_WRITE)
</code>
As you have <code>bytes(1)</code>, which is <code>\x01</code> and <code>bytes(2)</code
