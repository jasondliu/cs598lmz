from bz2 import BZ2Decompressor
BZ2Decompressor
import gzip
import zipfile
def decompress_file(file):
    file.seek(0)
    if file.read(2) == b'\x1f\x8b':
        file.seek(0)
        return gzip.GzipFile(fileobj=file)
    elif file.read(3) == b'BZh':
        file.seek(0)
        return BZ2Decompressor().decompress(file.read())
    file.seek(0)
    return file
def decompress_directory(directory):
    for filename in os.listdir(directory):
        file = open(os.path.join(directory, filename), 'rb')
        decompressed_file = decompress_file(file)
        with open(os.path.join(directory, os.path.splitext(filename)[0]), 'w') as f:
            f.write(decompressed_file.read().decode())
decompress_directory('../data/notebooks/')

# example:
# file = open(os.path.join
