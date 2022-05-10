import lzma
# Test LZMADecompressor.
compressor = lzma.LZMADecompressor()
decompressed_data = b''.join(compressor.decompress(data) for data in iter(lambda: f.read(1024 * 1024), b""))
</code>
generate "invalid start byte" exception, but this also works well:
<code>with open("lzma.7z", "rb") as f:
    import lzma
    # Test LZMADecompressor.
    decompressed_data = b''.join(lzma.decompress(data) for data in iter(lambda: f.read(1024 * 1024), b""))
</code>
so I am confused about these two ways about decompress. I know that LZMADecompressor is a class, it's a instance, but why the class can not work well just like the function, is it a bug?
I have searched the issues about lzma.LZMADecompressor, but I can't find any, so I write this question, hope someone can help me solve it.
thx very much!


A
