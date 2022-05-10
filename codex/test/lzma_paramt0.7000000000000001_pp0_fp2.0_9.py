from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor()

def get_data_file(filename):
    """
    get_data_file: get data file from pacman data folder
    """
    path = os.path.join(os.path.dirname(__file__), 'data', filename)
    if path.endswith('.gz'):
        return gzip.open(path, 'rb')
    elif path.endswith('.xz'):
        return LZMADecompressor(filename=path)
    else:
        return open(path, 'rb')

def get_data_file_size(filename):
    """
    get_data_file_size: get file size in bytes
    """
    path = os.path.join(os.path.dirname(__file__), 'data', filename)
    return os.path.getsize(path)

def get_data_file_size_in_mb(filename):
    """
    get_data_file_size_in_mb: get file size in megabytes
    """
    return
