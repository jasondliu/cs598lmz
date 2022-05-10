import lzma
# Test LZMADecompressor

def read_all(decompressor, file_size):
    """Read all data from the decompressor object."""
    data = b''
    while True:
        chunk = decompressor.unconsumed_tail
        if chunk:
            data += chunk
        if len(data) >= file_size:
            break
        chunk = decompressor.decompress(b'\x00' * (file_size - len(data)))
        if chunk:
            data += chunk
        if len(data) >= file_size:
            break
    return data

with open('test.lzma', 'rb') as f:
    cdata = f.read()

decompressor = lzma.LZMADecompressor()
