import lzma
lzma.decompress(in_file.read())
</code>
You'll note that the .xz decompression code is exactly the same as the code to decompress the .lzma file.
This is because the .xz file format was designed to be as simple as possible. It's just a simple header followed by LZMA1 compressed data (which is supported by the LZMA SDK).

