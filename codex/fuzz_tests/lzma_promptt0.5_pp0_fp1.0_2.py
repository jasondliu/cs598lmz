import lzma
# Test LZMADecompressor for decompression of files

def test_lzma():
    with lzma.open('test.xz') as f:
        file_content = f.read()
    print(file_content)
    print(type(file_content))

if __name__ == "__main__":
    test_lzma()
