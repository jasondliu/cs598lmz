import lzma
# Test LZMADecompressor
WORKER_NUM = 5
INDEX_VALUE = 7

def decompress(compressor, source_data):
    chunks = []
    while True:
        chunk = compressor.decompress(source_data)
        if chunk:
            chunks.append(chunk)
            source_data = None
        else:
            break
    return chunks

def lzmadata(source_file_path, worker_num, index_value):
    with open(source_file_path, 'rb') as f:
        compressor = lzma.LZMADecompressor(format=lzma.FORMAT_RAW, check=lzma.CHECK_NONE)
        chunks = decompress(compressor, f)
    
    # Summation
    result = 0
    for chunk in chunks:
        for byte in chunk:
            result += byte
            result *= worker_num
            result &= 255
            result ^= index_value
    return bytes([result])

if __name__ == '__main__':
    flag = lzmadata('dist/
