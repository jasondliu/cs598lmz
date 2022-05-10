import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
with open('data/enwik8_lzma', 'rb') as f:
    data = f.read(1024)
    while data:
        decompressed = decompressor.decompress(data)
        if decompressed:
            print(decompressed)
        data = f.read(1024)

# Test LZMAFile
with lzma.open('data/enwik8_lzma', 'rb') as f:
    print(f.read(1024))

# Test LZMAError
try:
    lzma.decompress(b'\x00' * 10)
except lzma.LZMAError as e:
    print(e)

# Test LZMAFilter
filters = [
    {'id': lzma.FILTER_LZMA1, 'dict_size': 2 ** 23, 'lc': 3, 'lp': 0, 'pb': 2},
    {'id': lzma.FILTER_X86, 'dict_size
