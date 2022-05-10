import bz2
# Test BZ2Decompressor

with bz2.BZ2Decompressor(buffering=1000) as decomp:
    size_print(decomp.decompress(compressed_data))
    try:
        size_print(decomp.decompress(compressed_data))
    except EOFError:
        print('caught expected EOFError')
# Many filter objects can be used in succession in a cascade

decomp = BZ2Decompressor()
decomp = compress_logs(decomp)

with FileOpener(filename, 'rb') as fh:
    while True:
        chunk = fh.read(2048)
        if not chunk:
            break

        next_chunk = decomp.decompress(chunk)
        sys.stdout.write(next_chunk.decode('utf-8'))

assert fh.closed
 
# Filter objects like compressors and decompressors can also be chained directly
with open('chained.bz2', 'rb') as fh:
    with bz2.BZ2Decompressor() as decomp
