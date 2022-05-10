import lzma
lzma.decompress(data)
</code>
I'm getting the error:
<code>ValueError: Incorrect length of data passed for decompression.
</code>
What am I doing wrong?


A:

You are reading the data as text, which is not what you want.
<code>with open('input.xz', 'rb') as f:
    data = f.read()
</code>

