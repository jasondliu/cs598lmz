import bz2
# Test BZ2Decompressor before creating the file instance
compress = bz2.BZ2Compressor()
decompress = bz2.BZ2Decompressor()

with open('compressed.txt', 'wb') as compressedFile:
    with open('original.txt', 'rb') as originalFile:
        while True:
            chunk = originalFile.read(10240)
            if len(chunk) == 0:
                break
            compressedFile.write(compress.compress(chunk))
    compressedFile.write(compress.flush())


with open('compressed.txt', 'rb') as compressedFile:
    with open('result.txt', 'wb') as resultFile:
        while True:
            chunk = compressedFile.read(10240)
            if len(chunk) == 0:
                break
            resultFile.write(decompress.decompress(chunk))
