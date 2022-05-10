import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress
lzma_compress_level = lzma.PRESET_EXTREME

def lzma_decompress_to_string(compressed_data):
    return lzma_decompress(compressed_data).decode('utf_8', 'replace')

#def lzma_compress_from_string(string_data):
#    string_data = string_data.encode('utf_8', 'replace')
#    return lzma_compress(string_data, lzma_compress_level)

def lzma_compress_from_string(string_data):
    string_data = string_data.encode('utf_8', 'replace')
    return lzma_compress(string_data)

# for testing
if __name__ == '__main__':
    string_data = 'some test data'
