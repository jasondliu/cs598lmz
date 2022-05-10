import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(),0)
    print(m[0:1])
    m[0:1] = bytes(2)
    print(m[0:1])

with open('test', 'rb') as f:
    print(f.read(1))
</code>
It outputs:
<code>b'\x01'
b'\x02'
b'\x01'
</code>
In contrast, if I just do:
<code>with open('test','wb') as f:
    f.seek(0)
    f.write(bytes(2))
with open('test','rb') as f:
    print(f.read(1))
</code>
The output is correctly <code>b'\x02'</code>. I can't figure out what the difference is. What am I doing wrong?


A:

Well, I would say you're forgetting to flush:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:

