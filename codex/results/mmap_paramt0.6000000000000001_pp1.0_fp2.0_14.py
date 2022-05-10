import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
    m.close()

with open('test', 'rb') as f:
    print(f.read())

&lt;/code&gt;</code></pre>
</blockquote>
If I run this in python 2.7 it works as expected, but in 3.4 it doesn't. In 3.4 I get the error: 
<blockquote>
<p>TypeError: an integer is required (got type bytes)</p>
</blockquote>
Is there a way to get this working in python 3.4?


A:

<code>bytes(2)</code> is a <code>bytes</code> object containing two <code>\x00</code> bytes. You want a <code>bytes</code> object containing a single <code>\x02</code> byte. Use <code>bytes([2])</code>.

