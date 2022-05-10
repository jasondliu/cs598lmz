import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'a'
    m.close()
</code>
When I run this code in python 3.6.0 I get the following error:
<code>Traceback (most recent call last):
  File "C:/Users/user/Desktop/test.py", line 7, in &lt;module&gt;
    m[0] = b'a'
TypeError: a bytes-like object is required, not 'str'
</code>
I get the same error in python 3.6.1.
The code works fine in python 3.5.2.
Does anyone know what's going on here?


A:

The documentation says:
<blockquote>
<p><code>&lt;code&gt;mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])&lt;/code&gt;</code></p>
<p>...</p>
<p>The buffer size must be less than or equal to the file size.</p>
</blockquote>
So you need to specify the
