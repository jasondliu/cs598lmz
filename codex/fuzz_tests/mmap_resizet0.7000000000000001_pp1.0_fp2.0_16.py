import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    f.write(a)
</code>
or 
<code>with open('test', 'w+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    f.write(a)
</code>
or 
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    m.close()
    f.truncate(0)
    f.write(a)
</code>
or 
<code>with open('test', 'w+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    m.close()
    f.truncate(0)
    f.write(a)
</code>
I still can't get this to work.  I'd rather not use <code>os.remove()</
