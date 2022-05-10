import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

def lzma_compress_str(s):
    return lzma_compress(s.encode('utf-8'))

def lzma_decompress_str(s):
    return lzma_decompress(s).decode('utf-8')

def compress_string(string, method=lzma_compress_str):
    return base64.b64encode(method(string)).decode('utf-8')

def decompress_string(string, method=lzma_decompress_str):
    return method(base64.b64decode(string))

def compress_string_gzip(string):
    return compress_string(string, gzip.compress)

def decompress_string_gzip(string):
    return decompress_string(string, gzip.decompress)

def compress_string_bz2(string):
    return compress_string(string, b
