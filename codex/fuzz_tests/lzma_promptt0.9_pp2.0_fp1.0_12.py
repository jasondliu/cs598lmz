import lzma
# Test LZMADecompressor class directly

decompressor = lzma.LZMADecompressor()

with open('../test/testdata/compressed.xz', 'rb') as in_file:
    data = in_file.read(1)

    while data:
        try:
            chunk_size = decompressor.get_decompress_size()
        except lzma.LZMAError as error:
            if error.message != "Output buffer is full":
                raise

        if chunk_size is None:
            chunk_size = len(data)*4

        chunk = decompressor.decompress(data, chunk_size)
        print('chunk size: ')
        print(chunk_size)

        if chunk:
            sys.stdout.write(chunk)
            # print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            # print(chunk)
            # print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

        data = in_file.read(1)
# Test LZMADecompressor class directly with XZFile

decompressor = lzma.LZMAD
