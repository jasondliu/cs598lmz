import bz2
bz2.BZ2File.close()

def _bz2_filter(data):
    '''
    Filter used in conjunction with the gzip module that handles opening bz2
    files
    '''
    return bz2.decompress(data)


def _bz2_open(filename):
    '''
    Return a file-like object that handles opening bz2 files
    '''
    return gzip.GzipFile(filename, mode='rb', fileobj=bz2.BZ2File(filename))


if bz2_available is True:
    salt.utils.gzip_util.GzipFile.close = _bz2_close
    salt.utils.gzip_util.open = _bz2_open
    # Let's also add bz2 to the list of supported compressions
    salt.utils.gzip_util.COMPRESSION_TYPES['bz2'] = _bz2_filter
