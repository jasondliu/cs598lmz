import lzma
# Test LZMADecompressor, test_count=1000
def test_lzma_decompressor_1000():
    #test_count = 1000
    test_count = 1
    # test_count = 10
    read_size_1 = 1024
    read_size_2 = 1024
    test_size = 1024 * 1024 * 4
    # test_size = 1024 * 1024 * 1024 * 10

    source_data = bytearray(random.getrandbits(8) for _ in range(test_size))
    print('prepare source data')
    for i in range(0, test_count):
        print(i)
        with lzma.open('test_lzma/source_data.lzma', 'wb', preset=9 | lzma.PRESET_EXTREME) as f_out:
            f_out.write(source_data)
        print('compress')
        with lzma.open('test_lzma/source_data.lzma', 'rb') as f_in:
            print('lzma.open')
