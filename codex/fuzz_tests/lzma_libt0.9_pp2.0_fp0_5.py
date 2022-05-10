import lzma
lzma.filter(data)
</code>
I would expect this code to raise an exception if the data is not valid, but it does not, it just looks like a 5x or so slowdown. Is there a way to actually check whether the data is valid LZMA, or is it possible to optimize the decompression in that case?


A:

You can try decompressing it and catching the exception.
<code>import lzma

try:
    decompressed = lzma.decompress(data)
    print('Valid lzma data.')
except lzma.LZMAError as e:
    print(e)
    print('Invalid lzma data.')
</code>

