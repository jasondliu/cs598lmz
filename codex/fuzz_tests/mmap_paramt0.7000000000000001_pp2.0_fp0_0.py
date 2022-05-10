import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    print(m[0:1])
    m[0] = b'\x00'
    print(m[0])
    m[0:1] = b'\x00'
    print(m[0])
</code>
output:
<blockquote>
<p>49</p>
<p>b'1'</p>
<p>0</p>
<p>48</p>
</blockquote>

