import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    m[0] = b'\x00'
    m.flush()
</code>
This works fine on Windows, but on Linux I get an <code>OSError</code> exception with the message <code>Invalid argument</code>. I've tried various combinations of <code>mmap.ACCESS_*</code> flags, but no luck.
What am I doing wrong?


A:

You need to specify the length of the file when you create the <code>mmap</code> object:
<code>m = mmap.mmap(f.fileno(), 1)
</code>
From the docs:
<blockquote>
<p>mmap(fileno, length[, flags[, prot[, access[, offset]]]])</p>
<p>Create a new memory-mapped file object. The arguments are the same as for the <code>&lt;code&gt;os.open()&lt;/code&gt;</code> function. The size of the mapped region must not exceed the size of the file.</p>
</
