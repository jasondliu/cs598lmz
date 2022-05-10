from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(f.read(pos))

if __name__ == '__main__':
    #bzcat('/home/rebecca/Downloads/enwiki-links.bz2', 879000000)
    with open('/home/rebecca/Downloads/enwiki-links.bz2', 'rb') as f:
        print(BZ2Decompressor().decompress(f.read(879000000)))
