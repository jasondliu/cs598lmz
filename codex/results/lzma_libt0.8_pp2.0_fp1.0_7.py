import lzma
lzma.LZMADecompressor()(open('foo.xz', 'rb').read()).decode('utf-8')

# Note the order of the parameters: `data`, then `mode`, then `encoding`,
# then `errors`
&gt;&gt;&gt; zlib.decompress(b'x\x9c+\xcf\xcd\x81\x01'), # passed only `data`
'Hello, world!\n'

&gt;&gt;&gt; zlib.decompress(b'x\x9c+\xcf\xcd\x81\x01', 16+zlib.MAX_WBITS), # passed `data` and `mode`
'Hello, world!\n'

&gt;&gt;&gt; zlib.decompress(b'x\x9c+\xcf\xcd\x81\x01', 16+zlib.MAX_WBITS, 'utf-8'), # passed `data`, `mode`, and `encoding`
'Hello, world!\
