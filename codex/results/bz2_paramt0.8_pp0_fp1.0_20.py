from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(encoded_data)

encoded_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# It is a tar file.
# https://docs.python.org/3/library/tarfile.html
from tarfile import TarFile
tar = TarFile.open(fileobj=io.BytesIO(BZ2Decompressor().decompress(encoded_data)))

# Like `tar tf`, but it returns a file-like object for each file instead of file name.
# https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractfile
def extract_members(tar, verbose):
    """Yield each member of a tar as a file-like object."""
    for member in tar.getmembers():
       
