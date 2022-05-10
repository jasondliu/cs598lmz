import lzma
lzma_name, lzma_ext = lzma.LZMAFile.name, lzma.LZMAFile.extensions
import bz2
bz2_name, bz2_ext = bz2.BZ2File.name, bz2.BZ2File.extensions
import zipfile
zip_name, zip_ext = zipfile.ZipFile.name, zipfile.ZipFile.extensions
import tarfile
tar_name, tar_ext = tarfile.TarFile.name, tarfile.TarFile.extensions


def get_encoding(file_name, encoding_exceptions=None):
    # file_name should be ascii.
    if isinstance(file_name, bytes):
        file_name = file_name.decode('ascii')
    if os.path.sep not in file_name and os.path.altsep not in file_name:
        return 'us-ascii'
    encodings = [
        'utf-8',
        getpreferredencoding(False),
        sys
