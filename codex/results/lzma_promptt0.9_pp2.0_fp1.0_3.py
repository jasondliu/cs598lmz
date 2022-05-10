import lzma
# Test LZMADecompressor for pathlib file
with lzma.open ('foo.7z') as f:
    print(f.readline()) 
</code>
Output:
<code>b'\x1b+\xb5LZMA\x00\x03'
</code>
But i dont want it.

