import bz2
# Test BZ2Decompressor to see if it can handle the file
fileobj = bz2.BZ2File(compressed_filename)
try:
    data = fileobj.read()
except Exception as e:
    fileobj.close()
    print(f'Error decompressing {compressed_filename}: {e}')
fileobj.close()

if len(data) != size:
    print(f'Corrupted data: size should be {size}, is {len(data)}')
else:
    # Decompress to the decompressed filename
    decompressed_filename = compressed_filename[:-4]
    print(f'Output to {decompressed_filename}')
    output = open(decompressed_filename, 'wb')
    output.write(data)
    output.close()
