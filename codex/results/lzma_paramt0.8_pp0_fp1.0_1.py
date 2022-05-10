from lzma import LZMADecompressor
LZMADecompressor()

from os import remove

lzma_path = "./results/lzma_"
def lzma_compress(txt_path, lzma_path, ipath):
    ifile = open(txt_path, 'rb')
    ofile = lzma.LZMAFile(lzma_path + ipath, 'wb')
    data = ifile.read()
    ofile.write(data)
    ofile.close()
    ifile.close()

def lzma_decompress(txt_path, lzma_path, ipath):
    ifile = lzma.LZMAFile(lzma_path + ipath, 'rb')
    ofile = open(txt_path, 'wb')
    data = ifile.read()
    ofile.write(data)
    ofile.close()
    ifile.close()

def main():
    txt_path = "./results/txt/"
    ipath = ""
    for i in range(1, 10):
        ipath = str(
