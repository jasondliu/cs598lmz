import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Gives the error:
<blockquote>
<pre><code>&lt;code&gt;Traceback (most recent call last):
  File "test_mmap_truncate.py", line 10, in &amp;lt;module&amp;gt;
    a = m[:]
ValueError: mmap closed or invalid
&lt;/code&gt;</code></pre>
</blockquote>
Why does this not work? From the documentation it seems like this should be possible:
<blockquote>
<p>mmap.__del__() This instance method should be called when the mmap object is
  no longer needed. It will be automatically invoked by Python when the
  instance is about to be destroyed, but you can also invoke it yourself
  when desired.</p>
</blockquote>
So I conclude that the <code>m</code> variable should be invalidated when the <code>with</code> block is exited, shouldn't it? What am I missing?


A:

If you want to do that, then you should keep the file data buffer in your code and
