import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
This code works fine on Windows, but on Linux it throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = b'\x00'
ValueError: mmap assignment is not supported
</code>
Is there a way to make this work on Linux?


A:

You need to open the file with <code>mmap.ACCESS_WRITE</code> access:
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
</code>
From the docs:
<blockquote>
<p>The <code>&lt;code&gt;access&lt;/code&gt;</code> argument determines the <code>&lt;code&gt;mmap&lt;/code&gt;</code> access policy. It defaults to <code>&lt;code&gt;ACCESS
