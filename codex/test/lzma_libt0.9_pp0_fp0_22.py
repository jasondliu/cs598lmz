import lzma
lzmac = lzma.LZMACompressor()

def init():
    global path, bucket, key_name, data
    path = '/Users/cyan/Downloads/rawdata/'
    bucket = 'result-netease'
    key_name = '/rawdata/'
    data = [f for f in listdir(path) if isfile(join(path, f))]


