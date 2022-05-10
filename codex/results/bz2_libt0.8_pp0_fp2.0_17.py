import bz2
bz2.decompress(bz2.compress(bytes(inp, 'utf-8')))

inp = '1' * 100000000

bz2.compress(bytes(inp, 'utf-8'))

bz2.decompress(bz2.compress(bytes(inp, 'utf-8')))

bz2.compress('1' * 100)
import lzma
lzma.decompress(lzma.compress(bytes(inp, 'utf-8')))
lzma.decompress(lzma.compress(bytes('1' * 100000000, 'utf-8')))

lzma.compress('1' * 100000000)
lzma.decompress(lzma.compress('1' * 100000000))
import lz4.frame
lz4.frame.decompress(lz4.frame.compress(bytes(inp, 'utf-8')))
import snappy
snappy.decompress(bytes(snappy.compress(bytes(
