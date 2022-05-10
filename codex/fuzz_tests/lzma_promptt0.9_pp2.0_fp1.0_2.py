import lzma
# Test LZMADecompressor individually
c = lzma.LZMADecompressor()
result = b""
with open("/sbin/initrd.img-4.4.0-134-generic", "rb") as f:
    for block in iter(lambda: f.read(64 * 1024), b""): # 64 KB
        try:
            result += c.decompress(block)
        except EOFError:
            break
result

# Test LZMADecompressor using context manager
file_data = b""
with lzma.LZMADecompressor() as c_mgr:
    with open("/sbin/initrd.img-4.4.0-134-generic", "rb") as f:
        file_data = c_mgr.decompress(f.read())
file_data
# Test LZMADecompressor using StreamingDecompressor
file_data = b""
with open("/sbin/initrd.img-4.4.0-134-generic", "rb") as f:
    with lzma.StreamingDec
