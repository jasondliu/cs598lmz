import bz2
bz2.decompress(archive_data)

with open(file_path, 'rb') as f:
    file_data = f.read()
    file_data == bz2.decompress(archive_data)
</code>

