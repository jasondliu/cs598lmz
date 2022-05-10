import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes
</code>
The commented out code is what does the writing I actually want, but I just included the other to see what I had to do for bytes. The error that I get is
<blockquote>
<p>TypeError: 'type' object does not support buffer interface</p>
</blockquote>
How am I supposed to turn an object into bytes? Or is there a way to pass an object by reference with mmap?


A:

How to convert objects to & from bytes is answered here: Convert python object to a string
For the sake of completeness I'll paste a sample code (but this is not your case, right?)
<code>import pickle
a = 42
# d.dumps() dumps an object to a byte stream
s = pickle.dumps( a )
# d.loads() loads an object from a byte stream
a = pickle.loads( s )
</code>

