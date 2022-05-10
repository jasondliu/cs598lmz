import bz2
# Test BZ2Decompressor
print('=' * 10, "Testing BZ2Decompressor.", '=' * 10)
# Get the compressed bytes
with bz2.open('../data/compressed/compressed_file.bz2', mode='rb') as zf:
        print('-' * 50)
        print('zf.name:', zf.name)
        print('Compressed file size:', zf.seekable().tell())
        print('-' * 50)
        compressed = zf.read()
        print('Bytes in the compressed file:', len(compressed))
        print('-' * 50)
        
# Create a decompressor
obj = bz2.BZ2Decompressor()
try:
        # Check that the decompressor doesn't have any content
        print('Decompressor has no data', 'len(obj.unused_data) =', len(obj.unused_data))
        chunk = obj.decompress(compressed)
        # The decompressed chunks are 1.5Kb large by default.
        print('Decompressed chunk size:', len(chunk))
