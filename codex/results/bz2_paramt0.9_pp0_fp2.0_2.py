from bz2 import BZ2Decompressor
BZ2Decompressor().decompress('text')

from sys import stdout
# f = BZ2File('compressed_file.bz2', 'wb', compresslevel=9)
# f.write('this is data')
# f.close()
compressed_data = open('compressed_file.bz2', 'rb')
decompressor = BZ2Decompressor()
for block in iter(lambda: compressed_data.read(100), ''):
    stdout.write(decompressor.decompress(block))
