import lzma
# Test LZMADecompressor
cd = lzma.LZMADecompressor()
# Test LZMACompressor
cc = lzma.LZMACompressor()

# Test LZMAFile
def read_file(path):
    with open(path, "rb") as f:
        return f.read()

def write_file(path, data):
    with open(path, "wb") as f:
        f.write(data)

def read_file_lzma(path):
    with lzma.open(path, "rb") as f:
        return f.read()

def write_file_lzma(path, data):
    with lzma.open(path, "wb") as f:
        f.write(data)

def check_file(path):
    with open(path, "rb") as f:
        return f.read()

def test_normal_file(path):
    data = read_file(path)
    write_file("tmp", data)
    assert check_file("tmp") == data

