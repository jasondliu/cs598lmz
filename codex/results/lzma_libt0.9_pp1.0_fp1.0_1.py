import lzma
lzma.open('xc-f2-s0.7_0.083-cluster.pckl.xz')
</code>
If I only have the string, what is the best way to convert it to a file?


A:

In Python 3, you can use the <code>BytesIO</code> class in <code>io</code> module:
<code>import io
import lzma

with lzma.open(io.BytesIO(my_str)) as f:
    data = f.read()
</code>
If you are using Python 2, you can use <code>StringIO</code>:
<code>import StringIO
import lzma

with lzma.open(StringIO.StringIO(my_str)) as f:
    data = f.read()
</code>

