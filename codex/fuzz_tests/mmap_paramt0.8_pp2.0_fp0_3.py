import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    try:
        m[0] = b'\x00'
    finally:
        m.close()
</code>
Note: I'm using Python 3.5 here.


A:

From the docs 
<blockquote>
<p>The mmap module defines the following exception:</p>
<pre><code>&lt;code&gt;exception mmap.error(args)
&lt;/code&gt;</code></pre>
<p>Exception raised on mmap() errors. The constructor takes the same
  arguments as from errno.error().</p>
</blockquote>
It's also documented as a subclass of <code>OSError</code>
<code>% python3
Python 3.5.1 (default, Dec  7 2015, 12:58:09) 
[GCC 5.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; isinstance(mmap.error(), OSError)
True
</code>

