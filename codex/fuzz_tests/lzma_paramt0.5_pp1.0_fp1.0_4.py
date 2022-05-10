from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor()

def decompress(compressed_data):
    return LZMADecompressor.decompress(compressed_data)

def write_to_file(data):
    with open('output.txt', 'wb') as f:
        f.write(data)

def main():
    with open('input.txt', 'rb') as f:
        data = f.read()
    decompressed_data = decompress(data)
    write_to_file(decompressed_data)

if __name__ == '__main__':
    main()
