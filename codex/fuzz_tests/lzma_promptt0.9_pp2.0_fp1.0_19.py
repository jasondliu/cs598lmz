import lzma
# Test LZMADecompressor by decompressing a single-byte compressed stream.
c = lzma.LZMADecompressor()
assert c.decompress(b'\x00\x01\x00') == b'a'
assert c.unused_data == b'\x01'
assert not c.eof

# Test by decompressing a stream that's split into 10-byte chunks.
c = lzma.LZMADecompressor()
buf = b''
for i in range(256):
    s = i.to_bytes(1, 'big') * 10
    buf += c.decompress(s, 10)
assert len(buf) == 10 * 256
assert buf[:10] == b'\x00' * 10
assert c.eof
# Test compressing and decompressing some data.
for datum in (b'hello ', b'there ', b'world\n', b'multi-byte unicode: \xe4\xb8\x96\xe7\x95\x8c\n', b'\x00\x01\x02\x
