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
print(view)
</code>
I expect <code>print(view)</code> to output <code>b''</code> as the <code>BufferedReader</code> should have been destroyed by the time <code>print(view)</code> is executed.
I have used the standard <code>io</code> module as an example, but the same thing happens with <code>socket</code> and <code>ssl</code> too.
Is there a way for me to prevent <code>view</code> from being destroyed?


A:

<blockquote>
<p>Is there a way for me to prevent <code>&lt;code&gt;view&lt;/code&gt;</code> from being destroyed?</p>
</blockquote>
Probably not.
What happens is that when a file-like object is closed, the underlying buffer is set to <code>None</code>. A <code>io.BufferedReader</code> stores its buffer in the <code>raw</code> attribute.
<code>&gt;&gt;&gt; def readinto(self, buf
