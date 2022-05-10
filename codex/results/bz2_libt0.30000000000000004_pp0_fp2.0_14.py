import bz2
bz2.decompress(compressed_data)

# Compress a file
import bz2
uncompressed_data = b'We are no longer the Knights who say Ni!'
with open('uncompressed.txt', 'wb') as f:
    f.write(uncompressed_data)
with open('uncompressed.txt', 'rb') as f_in, bz2.open('compressed.bz2', 'wb') as f_out:
    f_out.writelines(f_in)

# Decompress a file
import bz2
with bz2.open('compressed.bz2', 'rb') as f:
    file_content = f.read()
file_content

# Compress a file using a context manager
import bz2
uncompressed_data = b'We are no longer the Knights who say Ni!'
with open('uncompressed.txt', 'wb') as f:
    f.write(uncompressed_data)
with open('uncompressed.txt', 'rb') as f_in, bz2.open
