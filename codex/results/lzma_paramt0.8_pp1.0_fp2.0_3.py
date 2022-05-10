from lzma import LZMADecompressor
LZMADecompressor().decompress(part.content)

# or better just
bytes_io = io.BytesIO(part.content)
XZFile(bytes_io)

# Extract and run the downloaded file, e.g.
with XZFile(bytes_io) as f:
    subprocess.run(['/bin/bash', f.name])
</code>

