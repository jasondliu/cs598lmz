import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
It outputs nothing, it should output <code>b'\x01'</code>. When I use <code>mmap.mmap.seek</code> to change position of <code>m</code> before reading I get <code>ValueError: invalid argument</code>. If I change <code>truncate</code> to <code>close</code> or just <code>f.fileno()</code> in <code>mmap</code>, it works as expected. Is there a way to read and write to a file using <code>mmap</code>?


A:

The error you've come across is because the file will get truncated to zero-length in the first line of your <code>with</code> block
<code>f.write(bytes(1))
</code>
meaning that when you later come to map the file with
<code>mmap.mmap(f.fileno(), 0)
</code>
the offset and length arguments for the map will be invalid, leading to the <code>ValueError</code> you see. The "
