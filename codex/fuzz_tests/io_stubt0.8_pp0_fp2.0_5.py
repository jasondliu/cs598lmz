import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

view[0] = 42
EOF

# drop cache
echo 3 &gt; /proc/sys/vm/drop_caches
</code>
Then run the code. And run that again. You'll see it uses different memory each time.
How can I prevent it? I want the memory to be reused and that I don't have to manually clear the cache.


A:

<blockquote>
<p>My code at the bottom seems to allocate a new buffer every time.</p>
</blockquote>
Yes, that's how it is supposed to work.

<code>BytesIO</code> is a file object that allocates the buffer itself.
<code>RawIOBase</code> is an interface, which means that you need to implement it and return your own buffer. You do this by overriding <code>readinto</code> and <code>readable</code>.

When you do this, <code>BytesIO</code> calls <code>readinto</code> repeatedly. Since you're not returning the buffer, but instead a different buffer each time, you need to create a new buffer each time.
<
