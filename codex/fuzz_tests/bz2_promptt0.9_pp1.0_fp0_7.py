import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()
randstr = np.random.bytes(1000000)

randstr_bz2 = bz2.compress(randstr)

start = time.process_time()
decompressor.decompress(randstr_bz2)
end = time.process_time()

comptime = end-start

print(f'Decompression time: {comptime:.6f}')

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()

start = time.process_time()
compressor.compress(randstr)
end = time.process_time()

comptime = end-start

print(f'Compression time: {comptime:.6f}')

# Test file processing times

# Compression first

compressor = bz2.BZ2Compressor()

comp_elapsed = 0
for item in json_paths:
    start = time.process_time()
    with open(item
