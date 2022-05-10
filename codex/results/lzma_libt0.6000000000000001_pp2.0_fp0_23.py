import lzma
lzma.decompress(open('compressed_logs.xz','rb').read())

# Result
# b'This is some text.\n'
</code>

