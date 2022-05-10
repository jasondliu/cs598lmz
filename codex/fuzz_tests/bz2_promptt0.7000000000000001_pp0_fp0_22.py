import bz2
# Test BZ2Decompressor object
decompressor = bz2.BZ2Decompressor()

with bz2.BZ2File('example.bz2', 'rb') as input:
    with open('example.csv', 'wb') as output:
        for data in iter(lambda : input.read(100 * 1024), b''):
            decompressed = decompressor.decompress(data)
            if decompressed:
                output.write(decompressed)
            else:
                print('end of compressed data')
                break

# Test BZ2File.read()
with bz2.BZ2File('example.bz2', 'rb') as input:
    data = input.read()

# Test BZ2File.seek() and BZ2File.tell()
with bz2.BZ2File('example.bz2', 'rb') as input:
    print('%d bytes before decompression' % input.tell())
    data = input.read()
    print('%d bytes after decompression' % input.tell())
    input.seek(0)
   
