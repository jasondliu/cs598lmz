from lzma import LZMADecompressor
LZMADecompressor.CHECK_NONE = 0

def decompress_data(data):
    out = bytearray()
    decompressor = LZMADecompressor('CHECKSUM')
    
    while True:
        try:
            chunk = data.read(100 * 1024)
            out += decompressor.decompress(chunk)
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            break
        if len(chunk) < 100 * 1024:
            out += decompressor.flush()
            break
    return out

def get_data(url):
    out = bytearray()
    action, _, url = url.rpartition('://') + '://'
    assert action == 'lzma', "unknown action: " + action
    if url.startswith('file://'):
        filename = url[7:]
        with open(filename, 'rb') as data:
            out += decompress_data(data)
    elif url.startswith('http://') or url.startswith('https
