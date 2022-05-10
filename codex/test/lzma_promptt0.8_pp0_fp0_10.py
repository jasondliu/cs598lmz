import lzma
# Test LZMADecompressor
def decompress_lzma(source_path,target_path):
    read_file = lzma.open(source_path, mode='rb')
    # read_file = gzip.open(source_path, mode='rb')
    write_file = open(target_path, 'wb')
    data = read_file.read()
    write_file.write(data)
    read_file.close()
    write_file.close()

def compress_lzma(source_path,target_path):
    read_file = open(source_path, mode='rb')
    write_file = lzma.open(target_path, mode='wb', format=lzma.FORMAT_XZ)
    # write_file = gzip.open(target_path, mode='wb', compresslevel=9)
    data = read_file.read()
    write_file.write(data)
    read_file.close()
    write_file.close()

def decompress_lzma_by_bytes(compress_bytes):
    decomp
