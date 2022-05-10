import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(len(a)) # 0
</code>
If I don't use <code>mmap</code>, I get the expected behaviour:
<code>with open('test', 'r+b') as f:
    a = f.read()
    f.truncate()
    print(len(a)) # 1
</code>
Is there a way to get <code>len(a) == 1</code> without closing the file before calling truncate()?


A:

To keep the mmap object in sync, you have to flush it to disk using <code>mmap.flush()</code>:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.flush()
    f.truncate()
    a = m[:]
    print(len(a))
</code>
Output:
<code>0
</code>
But don't truncate a file to which
