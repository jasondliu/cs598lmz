import lzma
lzma.decompress(data)
</code>
Voilà! You get your decompressed data. Now, you can use the PIL library to save it as a JPEG file.
<code>import PIL.Image
with open("test.jpeg", "wb") as f:
    f.write(lzma.decompress(data))
</code>

