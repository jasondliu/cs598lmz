import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 2
    m.close()
    print(f.read())
</code>
The output is <code>b'\x01'</code> and not <code>b'\x02'</code> and I can't figure out why. The second argument to <code>mmap.mmap</code> specifies the size of the mapping, and I'm not sure what it should be. I've tried 0, 1, and 100 (arbitrarily large) and none of them work.


A:

<blockquote>
<p>The second argument to mmap.mmap specifies the size of the mapping, and I'm not sure what it should be.</p>
</blockquote>
It depends on whether you are using a fixed-size or dynamic-size file.
If you are using a fixed-size file, the second argument must match the size of the file.
If you are using a dynamic-size file, you can use the constant value <code>mmap.MAP_SHARED</code> instead of a numeric argument.

