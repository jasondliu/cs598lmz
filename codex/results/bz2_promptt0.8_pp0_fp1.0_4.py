import bz2
# Test BZ2Decompressor
with bz2.BZ2File('members.csv.bz2', 'rb') as cmpr_file, open('members.csv', 'wb') as out_file:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: cmpr_file.read(100*1024), b''):
        data = decompressor.decompress(block)
        out_file.write(data)
    out_file.write(decompressor.flush())
# Test BZ2Compressor
source_file = open('members.csv', 'rb')
with open('members.csv.bz2', 'wb') as target_file, bz2.BZ2File('members.csv.bz2', 'wb') as compressed_file:
    compressor = bz2.BZ2Compressor()
    for block in iter(lambda: source_file.read(100*1024), b''):
        data = compressor.compress(block)
        compressed_file.write(data)
    compressed_file.write(compressor.flush())

