import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
I'm getting the error
<blockquote>
<p>The truth value of a bytes-like object is ambiguous. Use <code>&lt;code&gt;a != b&lt;/code&gt;</code> to test for inequality.</p>
</blockquote>
What can I do to fix this? I'm running on Python 3.8.2 on windows.


A:

you can just convert it to <code>str</code> like this:
<code>a = str(m[:])
</code>

