from lzma import LZMADecompressor
LZMADecompressor
import tarfile

JPEG_QUALITY = 85
JPEG_SUFFIX = '.jpg'

BUFFER_SIZE = 4096

def update_progress(curr, n):
    progress = curr / n
    progress_int = int(progress * 20)
    print("\r [{}{}] {:0.0f}%".format("#" * progress_int,
    "-" * (20 - progress_int), progress * 100), end="")

def chunkify(f, size=1024*1024):
    chunk = f.read(size)
    while chunk:
        yield chunk
        chunk = f.read(size)

def extract_image(fobj, outfile, file_size, chunk_size=24*1024):
    data_remaining = file_size
    bytes_read = 0
    with open(outfile, 'wb') as out:
        for chunk in chunkify(fobj, chunk_size):
            out.write(chunk)
            bytes_read += len(chunk)
            update_progress(bytes_read,
