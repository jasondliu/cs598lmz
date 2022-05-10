from lzma import LZMADecompressor
LZMADecompressor

def uncompress(compressed):
    decompressor = LZMADecompressor()    
    return decompressor.decompress(compressed)

def tar_decompress(compressed, dst=False):
    if dst:
        dst_path = dst
    else:
        dst_path = os.path.join(os.path.dirname(file), 'data')
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)
    tar = tarfile.open(compressed)
    tar.extractall(path=dst_path)
    tar.close()
    
except Exception as e:
    print('{} decompress error!'.format('tar.xz'))
    raise(e)
try:
    import rarfile
    def rar_decompress(compressed, dst=False):
        if dst:
            dst_path = dst
        else:
            dst_path = os.path.join(os.path.dirname(file), 'data')
        if
