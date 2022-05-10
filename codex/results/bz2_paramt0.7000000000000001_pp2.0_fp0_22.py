from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(file_content)

# Writing compressed data
with open('compressed_file.bz2', 'wb') as f:
    f.write(compressed_data)

with open('somefile.bz2', 'rb') as f:
    decompressor = BZ2Decompressor()
    file_content = f.read()
    decompressed_data = decompressor.decompress(file_content)
    decompressed_data += decompressor.flush()

# Temporary files and folders
import tempfile
temp_file = tempfile.TemporaryFile()

# Named temporary file
temp_file_with_name = tempfile.NamedTemporaryFile()

# Temporary folder
with tempfile.TemporaryDirectory() as tmp_dir:
    print('Created temporary folder:', tmp_dir)

# Using archives
import shutil
with zipfile.ZipFile('files.zip', 'w') as z:
    z.write('file_one.txt')
    z.write('file_two.txt')

with zipfile.ZipFile('files.
