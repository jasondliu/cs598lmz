from bz2 import BZ2Decompressor
BZ2Decompressor.decompress
decompressor = BZ2Decompressor()
original_size = 0
data_size = 0
with open('../resource/log.bz2', mode='rb') as f:
    for line in f:
        original_size += len(line)
        data_size += len(decompressor.decompress(line))
    data = decompressor.flush()
    data_size += len(data)
    original_size += len(data)
print(f'Rate: {original_size / data_size:.2f}')

# zlib.decompressobj()
from zlib import decompressobj
decompressor = decompressobj()
original_size = 0
data_size = 0
with open('../resource/log.bz2', mode='rb') as f:
    for line in f:
        original_size += len(line)
        data_size += len(decompressor.decompress(line))
    data = decompressor.flush()
    data_size += len(data)
    original_size += len(data
