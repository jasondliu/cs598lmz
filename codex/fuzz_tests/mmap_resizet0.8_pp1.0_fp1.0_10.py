import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

print(a)
# b''
</code>
To fix this, you need to move the <code>m.close()</code> after the <code>f.truncate()</code>, because otherwise the <code>f.truncate()</code> will truncate to the size of the <code>mmap</code>:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    f.truncate()
    m.close()

print(a)
# b'\x00'
</code>
Not sure if this is intended behaviour or not, but the documentation is quite vague about it.

