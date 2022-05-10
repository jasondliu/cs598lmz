import lzma
lzma.decompress(open('/tmp/test.xz', 'rb').read())

# OUTPUT: b'hello world'
</code>

