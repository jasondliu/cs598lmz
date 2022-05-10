import lzma
# Test LZMADecompressor

with open('test.xz', 'rb') as f:
    d = lzma.LZMADecompressor()
    with d.stream(f) as decomp:
        for line in decomp:
            print(line)

# Test LZMAFile

with lzma.open('test.xz') as f:
    for line in f:
        print(line)

# Test LZMAFile with mode='w'

with lzma.open('test.xz', mode='w') as f:
    f.write(b'hello world\n')

with lzma.open('test.xz') as f:
    print(f.read())

# Test LZMAFile with mode='r'

with lzma.open('test.xz', mode='r') as f:
    print(f.read())

# Test LZMAFile with mode='a'

with lzma.open('test.xz', mode='a') as f:
    f.write(b'hello world\n')
