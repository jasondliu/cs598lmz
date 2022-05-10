import lzma
lzma.LZMAFile

from django.conf import settings


def check_xz_installed():
    if not hasattr(settings, 'SNAPSHOT_XZ_COMPRESSION'):
        return False
    try:
        import lzma
        lzma.LZMAFile
        return True
    except ImportError:
        return False


def compress_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    fout = filename + '.xz'
    with lzma.LZMAFile(fout, 'wb') as f:
        f.write(data)
    return fout


def decompress_file(filename):
    with lzma.LZMAFile(filename, 'rb') as f:
        data = f.read()
    fout = filename[:-3]
    with open(fout, 'wb') as f:
        f.write(data)
    return fout


def compress_string(data):
    f = BytesIO()
   
