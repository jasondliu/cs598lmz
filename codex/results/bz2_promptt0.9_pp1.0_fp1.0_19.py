import bz2
# Test BZ2Decompressor for its performance on small files.
data = data_file.open(data_file.ZIP_FILE, 'rb').read()
dec = bz2.BZ2Decompressor()

for loop in range(1000):
    for case in [0, 1]:
        if case:
            data = dec.decompress(data)
        pre_time = time()
        result = dec.decompress(data)
        post_time = time()
        delta = post_time - pre_time
        if delta:
            break
    if not delta:
        raise RuntimeError("bz2 not working properly")
    expect = len(data) * loop
    if len(result) != expect:
        raise RuntimeError("wrong length %d, expected %d" % (len(result), expect))

print("bz2 performance:", "%.2f MB/s" % (len(result)/1048576/delta))

# Test BZ2Compressor for its performance on small files.
data = data_file.open(data_file.ZIP_FILE, 'rb
