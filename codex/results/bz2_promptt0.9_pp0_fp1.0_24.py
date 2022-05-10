import bz2
# Test BZ2Decompressor
#
# >>> import bz2
# >>> d = bz2.BZ2Decompressor()
# >>> s = d.decompress(bz2_data, 1000)
# >>> len(s)
#       1230

def process_tar_gz(filename: bytes) -> list:
    decompressor = bz2.BZ2Decompressor()
    with open(filename, 'rb') as gz_file:
        magic = gz_file.read(2)
        if magic != b"\x1f\x8b":
            raise ValueError("Not a gzip file.")
    
        with gzip.GzipFile(fileobj=gz_file) as decomp:
            with tarfile.TarFile(fileobj=decomp) as tar:
                return tar.getnames()
            # decomp.extrabuf = b''
            # decomp.max_read_chunk = 2 ** 31 - 2
            # tar_data = decomp.read()
            # # tar.extractfile('./README').read()
            # return tar.get
