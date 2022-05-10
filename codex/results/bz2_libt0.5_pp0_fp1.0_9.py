import bz2
bz2_file = bz2.BZ2File('sample.bz2')
data = bz2_file.read()
bz2_file.close()

# compress data
import bz2
uncompressed_data = b'\n'.join(lines)
compressed_data = bz2.compress(uncompressed_data)

# compress data, chunk by chunk
import bz2
compressor = bz2.BZ2Compressor()
for chunk in chunks:
    compressed_chunk = compressor.compress(chunk)
    if compressed_chunk:
        write(compressed_chunk)
final_chunk = compressor.flush()
if final_chunk:
    write(final_chunk)

# read a zip file
import zipfile
zip = zipfile.ZipFile('spam.zip')
zip.namelist()
zip.getinfo('eggs.txt')
zip.read('eggs.txt')

# write a zip file
import zipfile
zip = zipfile.ZipFile('spam.zip', 'w
