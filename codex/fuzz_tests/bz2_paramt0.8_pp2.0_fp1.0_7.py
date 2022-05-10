from bz2 import BZ2Decompressor
BZ2DecompressorObject = BZ2Decompressor()

# Below function taken from http://stackoverflow.com/questions/17019962/using-bz2-file-in-python-3-3-as-a-file-object-and-not-a-bytes-object
def read_file_in_chunks(fileobj, chunk_size=1024*1024):
    """
    Read a file in chunks of bytes, where chunk size
    is passed in as the second argument (defaults to 1MB).
    """

    while True:
        data = fileobj.read(chunk_size)
        if not data:
            break
        yield data

# Create a file like object to hold the decompressed data
decompressed_file_object = io.BytesIO()

# Decompress the bz2 file and store the decompressed file in the file like object
for data_chunk in read_file_in_chunks(compressed_file):
    decompressed_data = BZ2DecompressorObject.decompress(data_chunk)
    if decompressed_data
