import bz2
# Test BZ2Decompressor and BZ2Compressor
for func in (bz2.decompress, bz2.compress):
    print(func.__name__)
    try:
        data = func(b'1234567890')
    except Exception as err:
        print('error:', err)
    else:
        print(data)
    print()
