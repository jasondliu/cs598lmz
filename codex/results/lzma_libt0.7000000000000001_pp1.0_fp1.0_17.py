import lzma
lzma.decompress(zipped)

def compress_file(filename):
    file = open(filename, "rb")
    zipped = lzma.compress(file.read())
    file.close()
    return zipped

def decompress_file(compressed):
    return lzma.decompress(compressed)

def compress_save_file(filename):
    file = open(filename, "rb")
    zipped = lzma.compress(file.read())
    file.close()
    file = open(filename, "wb")
    file.write(zipped)
    file.close()

def decompress_save_file(filename):
    file = open(filename, "rb")
    unzipped = lzma.decompress(file.read())
    file.close()
    file = open(filename, "wb")
    file.write(unzipped)
    file.close()

def compress_save_file_to(filename, destination):
    file = open(filename, "rb")
    zipped
