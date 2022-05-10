import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read())
    print(m.size())
    print(m.tell())
    print(m.readline())
    m.seek(0)
    print(m.readline())
    print(m.read_byte())
    m.write_byte(bytes(2))
    m.close()
</code>
Output:
<code>b'\x01'
1
0
b'\x01'
b'\x01'
Traceback (most recent call last):
  File "./test.py", line 16, in &lt;module&gt;
    print(m.read_byte())
ValueError: read byte out of range
</code>


A:

The problem is that your file only has a single byte (<code>b'\x01'</code>). Your <code>readline()</code> call reads that byte, but then leaves the file pointer at the end-of-file. There's nothing more to read, so the <code>read_byte()</code> call fails.
The <code>size()
