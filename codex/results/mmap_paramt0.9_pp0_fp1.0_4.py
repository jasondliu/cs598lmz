import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(256))
    m.close()

with open('test', 'rb') as f:
    size = os.path.getsize('test')
    print(size)
</code>
Outputs:
<code>1
</code>
Why the size was not changed to <code>256</code>?


A:

<code>mmap</code> only changes the meaning of what you read. <code>seek</code> and <code>tell</code> are still based on the original length of the file, and <code>os.path.getsize</code> is using the same position.
From the mmap documentation:
<blockquote>
<p>The mmap constructor is documented in the mmap module. Note that the <code>&lt;code&gt;offset&lt;/code&gt;</code> arg is not the same as the file pointer position - <code>&lt;code&gt;offset&lt;/code&gt;</code> gives the starting location of the map. It is usually a multiple of <code>&lt
