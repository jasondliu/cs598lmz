import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.size())
    m[0] = 4
    print(m[0])
    m.close()
</code>
I thought m.close() should close the mmap object. The code above works as it should if I comment out m.close(). If I don't close the mmap object then the file is locked until I exit the python program.
But if I un-comment the m.close() line, I get a TypeError: mmap closed.
It also doesn't work if I put the code inside a try/finally block and close the mmap object in the finally block.
I am using python 3.5.2 on Windows 10.


A:

<blockquote>
<p>You have to call <a href="https://docs.python.org/3.5/library/mmap.html?highlight=mmap#mmap.mmap.close" rel="nofollow noreferrer"><code>&lt;code&gt;mmap.close()&lt;/code&gt;</code></a> to release the resources associated with the map.</p>
