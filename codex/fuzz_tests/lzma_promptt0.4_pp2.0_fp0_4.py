import lzma
# Test LZMADecompressor

with open('/home/alex/Downloads/test.lzma', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    with decompressor:
        for block in iter(lambda: f.read(64 * 1024), b''):
            data = decompressor.decompress(block)
            if data:
                print(data)
            else:
                break

# Test LZMAFile

with open('/home/alex/Downloads/test.lzma', 'rb') as f:
    with lzma.open(f) as lzf:
        for line in lzf:
            print(line)

# Test LZMAFile with mode='r'

with lzma.open('/home/alex/Downloads/test.lzma', mode='r') as lzf:
    for line in lzf:
        print(line)

# Test LZMAFile with mode='w'

with lzma.open('/home/alex/Downloads
