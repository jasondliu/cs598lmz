from lzma import LZMADecompressor
LZMADecompressor(check=1)
'foo'.encode()
</code>
The second attempt runs slower and produces no result either.
<code>s = 'foo'
s = codecs.encode(s, encoding='ascii')

with lzma.open('sample.xz') as inp, \
     open('sample.txt', 'wb') as out:
    [inp.read(8)]
    decomp = LZMADecompressor(check=1)
    next_header_bytes = inp.read(8)
    if s not in next_header_bytes:
        raise Exception('Not found in XZ')
    while True:
        chunk = inp.read(64 * 1024)
        if not chunk:
            break
        out.write(decomp.decompress(chunk))
</code>
How do I decompress the complete library with the first match to the string <code>foo</code>?

