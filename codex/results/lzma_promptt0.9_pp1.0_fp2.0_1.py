import lzma
# Test LZMADecompressor

for divisor in [1, 2, 10, 100, 1000]:
    print('\x1b[34m')
    print('='*20, 'divisor =', divisor, '='*20)
    print('\x1b[0m')
    print('\t'.join(['u src', 'c src', 'u src size', 'c len', 'u src size', 'c src size']))

    # Create a unique data source
    src = []
    while len(src) < 1048576:
        src += [str(random.randrange(0, 256))]
    src = ''.join(src)

    # Create compressed source
    def compressor_factory_factory(size):
        def compressor_factory():
            return lzma.LZMACompressor(check=lzma.CHECK_CRC64, preset=0, filters=(
                {'id': lzma.FILTER_LZMA1, 'dict_size': size / divisor, 'lc': 0, 'lp': 0, 'pb': 0},
