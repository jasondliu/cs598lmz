import lzma
# Test LZMADecompressor

for divisor in [1, 2, 10, 100, 1000]:
    print('\x1b[34m')
    print('='*20, 'divisor =', divisor, '='*20)
    print('\x1b[0m')
    print('\t'.join(['u src', 'c src', 'u src size', 'c len', 'u src size', 'c src size']))

    # Create a unique data source
    src = []
