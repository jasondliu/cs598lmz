import lzma
# Test LZMADecompressor' input sizes.

# Non-integerize a number, e.g. '2.7' -> 2
def intfy(x):
    return int(str(x).split('.')[0])

for size in range(5, 10):
    size = 10 ** size
    print('Using size', size)
    decomp = lzma.LZMADecompressor()
    for n in range(intfy(size / 4), size, intfy(size / 8)):
        print('  Trying n =', n)
        print('    ', end='')
        chunksize = n // 10
