import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This gives me <code>b'\x01'</code> as expected.
Now I try to write the same thing using <code>io.BytesIO</code>
<code>import io
import mmap

f = io.BytesIO(bytes(1))
m = mmap.mmap(-1, 1)
m.write(f.getvalue())
f.truncate(0)
a = m[:]
print(a)
</code>
This gives me <code>b'\x00'</code> instead of <code>b'\x01'</code>.
I have tried this on Python 2.7, 3.4, and 3.5.
Why is there a difference between the two examples?


A:

The <code>mmap</code> module uses the <code>os.open()</code> function, which takes a <code>length</code> argument.
<blockquote>
<p>The length argument specifies the size of the file. The optional flags argument specifies how the file is to be opened. The default
