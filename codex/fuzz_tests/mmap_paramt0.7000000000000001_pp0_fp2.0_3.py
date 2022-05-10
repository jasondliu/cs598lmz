import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\0'
    m.close()
</code>
I would have expected that the <code>mmap</code> would close the file, but it doesn't:
<code>&gt;&gt;&gt; os.stat('test').st_size
1
</code>
I've done some digging, and found that the <code>mmap</code> is using the <code>open</code> function from the Python <code>io</code> library:
<code>&gt;&gt;&gt; mmap.mmap(0, 0)._fd
&lt;_io.FileIO name=0 mode='rb' closefd=False&gt;
</code>
The <code>closefd</code> argument is the one controlling whether the file is closed on file object deletion. It defaults to <code>True</code> in the Python <code>open</code> function, but it's <code>False</code> in the <code>io</code> <code>open</code> function.
Why is the <code>mmap</
