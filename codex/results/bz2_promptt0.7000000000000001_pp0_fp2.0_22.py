import bz2
# Test BZ2Decompressor and BZ2Compressor instances.

print('Reading BZ2 data from stdin...')
bz_in = BZ2Decompressor()
data = b''
while True:
    datum = sys.stdin.buffer.read(1024)
    if datum == b'':
        break
    data += bz_in.decompress(datum)
data += bz_in.flush()

print('\nWriting BZ2 data to stdout...')
bz_out = BZ2Compressor()
for i in range(0, len(data), 1024):
    sys.stdout.buffer.write(bz_out.compress(data[i:i+1024]))
sys.stdout.buffer.write(bz_out.flush())
