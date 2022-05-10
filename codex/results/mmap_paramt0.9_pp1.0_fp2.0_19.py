import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(list(m))
    m.close()
</code>
When running the above code, it gives
<code>[0]
</code>
But if I change <code>'r+b'</code> to <code>'r'</code>, it gives
<blockquote>
<p>ValueError: must have write enabled</p>
</blockquote>
I feel it a little confused. Could you help me out?


A:

If you have a writable file, this means that the data inside is writable as well.
If you open the file in read-only mode, and you only use it to read, then this means that you aren't going to modify it - but that doesn't mean you can't. If you want to prevent the file from being modified, you should use a separate file object, that has no permissions to modify the file (and no permissions to modify the file object in memory, because the file object points to the writable file, so it can modify the original file).

According to the docs of <code>mmap</code>:
<blockquote>
<p>The <
