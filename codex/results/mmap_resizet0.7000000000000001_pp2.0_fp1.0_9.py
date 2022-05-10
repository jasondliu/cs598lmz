import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>mmap.error: cannot resize a mapped array</code>. 
I tried a workaround like this:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
</code>
But this raises <code>ValueError: mmap closed or invalid</code>.
I'm not sure how to fix this. It seems that <code>f.truncate()</code> has no effect on the <code>mmap</code>. How can I make the <code>mmap</code> aware of the new size?


A:

You can use <code>resize</code> on the <code>mmap</code> before truncating the file:
<code>with open('test
