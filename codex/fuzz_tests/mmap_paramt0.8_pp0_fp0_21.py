import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(bytes(1))
    m.close()
</code>
and this is the error message that I am getting:
<code>Traceback (most recent call last):
  File "C:/Users/vkulakov/Desktop/tester.py", line 10, in &lt;module&gt;
    m.write(bytes(1))
TypeError: write() argument must be str, not bytes
</code>
I am wondering what I am doing wrong?


A:

The problem is that the <code>m.write()</code> method takes a <code>str</code> as an argument in Python 2.x, but you are passing it a <code>bytes</code> object.
From the <code>mmap</code> documentation (emphasis mine):
<blockquote>
<p>The <code>&lt;code&gt;mmap&lt;/code&gt;</code> constructor creates a memory-map to an existing file. This must be called with a file handle open for <strong>reading and
