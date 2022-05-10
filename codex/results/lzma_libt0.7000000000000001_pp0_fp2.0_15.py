import lzma
lzma_encode = lzma.compress
lzma_decode = lzma.decompress

def lzma_encode_file(filename, outfile=None):
    if outfile is None:
        outfile = filename + ".xz"
    with open(filename, "rb") as fin:
        with open(outfile, "wb") as fout:
            lzma_encode(fin, fout)

def lzma_decode_file(filename, outfile=None):
    if outfile is None:
        outfile = filename[:-3]
    with open(filename, "rb") as fin:
        with open(outfile, "wb") as fout:
            lzma_decode(fin, fout)


# 7z file
import subprocess
def sevenz_encode_file(filename, outfile=None):
    if outfile is None:
        outfile = filename + ".7z"
    subprocess.call(["7z", "a", "-t7z", outfile, filename])
