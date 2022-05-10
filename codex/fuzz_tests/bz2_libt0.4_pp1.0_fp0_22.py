import bz2
bz2.decompress(compressed_data)

# Compress and decompress byte data
import bz2
compressed_data = bz2.compress(original_data)
bz2.decompress(compressed_data)

# Compress and decompress files
import bz2
with open('file_path', 'rb') as input:
    with bz2.open('file_path.bz2', 'wb') as output:
        output.writelines(input)
with bz2.open('file_path.bz2', 'rb') as input:
    with open('file_path', 'wb') as output:
        for line in input:
            output.write(line)

# Compress and decompress files with a higher compression level
import bz2
with open('file_path', 'rb') as input:
    with bz2.open('file_path.bz2', 'wb', compresslevel=9) as output:
        output.writelines(input)
with bz2.open('file_path.bz2', '
