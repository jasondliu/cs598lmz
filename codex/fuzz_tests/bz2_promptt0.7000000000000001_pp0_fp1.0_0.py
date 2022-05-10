import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SY.\xc8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xf0\x01\x07n\x00?'

decompressor = bz2.BZ2Decompressor()

# Feed data in small chunks
decompressed_data = []

for chunk in [
    data[0:4],
    data[4:10],
    data[10:14],
    data[14:18],
    data[18:],
]:
    decompressed_data.append(decompressor.decompress(chunk))

decompressor.decompress(b'BZh91AY&SY')

# After decompressed_data has been consumed, the decompressor can be used again
decompressor.decompress(b'\x18\x00\x01>_\x80\x00\x10@\x02\xff\xf0\x01\x07n\x00?')

# Compressing data
comp
