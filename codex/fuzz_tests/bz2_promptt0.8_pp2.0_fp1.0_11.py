import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes'.format(len(data)))
decompressor = BZ2Decompressor()

for block in [data[:4], data[4:8], data[8:12], data[12:16]]:
    out = decompressor.decompress(block)
    if out:
        print('Output', repr(out), len(out))
    else:
        print('buffering...')

remaining = decompressor.flush()
print('Flushed out', repr(remaining))
# Test BZ2File
filename = 'bz2_file_example.bz2'
data = 'Contents of the example file go here.\n'

with bz2.BZ2File(
