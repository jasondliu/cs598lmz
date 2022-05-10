import bz2
bz2.decompress(file)
</code>
I get this error:
<code>TypeError: a bytes-like object is required, not '_io.TextIOWrapper'
</code>
I tried to open the file as binary using:
<code>file = open('file.bz2', 'rb')
</code>
But the error remains the same.
How can I fix this?


A:

You need to read the file first, then decompress it.
<code>with open('file.bz2', 'rb') as f:
    file = f.read()

bz2.decompress(file)
</code>

