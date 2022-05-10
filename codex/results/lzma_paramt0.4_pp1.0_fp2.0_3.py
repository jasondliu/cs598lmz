from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

#compress
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(data)
compressor.flush()

#compress to a file
compressor = LZMACompressor()
with open('compressed_file.xz', 'wb') as f:
    for part in iter(lambda: file_object.read(1024), b''):
        f.write(compressor.compress(part))
    f.write(compressor.flush())

#decompress from a file
decompressor = LZMADecompressor()
with open('compressed_file.xz', 'rb') as f:
    file_content = f.read()
    decompressed_data = decompressor.decompress(file_content)

#compress to a file with multithreading
import concurrent.futures
compressor = LZMACompressor()
with open('compressed_file.xz', 'wb') as f:
    with concurrent.futures.ThreadPoolExec
