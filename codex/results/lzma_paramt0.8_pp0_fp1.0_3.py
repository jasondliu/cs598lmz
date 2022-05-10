from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x00\x05\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x08\x04\x04\x01\x00\x104')

def write_bytes(data):
    with open('data.bin', 'wb') as f:
        f.write(data)

if __name__ == '__main__':
    write_bytes(b'\x00\x05\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x08\x04\x04\x01\x00\x104')
</code>


A:

For decompressing your .xz file you need to use the lzma module. Check the documentation here.
You will also need to import <code>LZMADecompressor</code>.

