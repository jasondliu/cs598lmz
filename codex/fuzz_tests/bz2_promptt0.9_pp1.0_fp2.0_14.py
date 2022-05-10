import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
with open('book.pdf.bz2', 'rb') as book:
    print(decompressor.decompress(book.read())[:100])

compressor = bz2.BZ2Compressor()
with open('book.compressed', 'wb') as file:
    file.write(compressor.compress(data))
    file.write(compressor.flush())
```
