import lzma
# Test LZMADecompressor
# https://pymotw.com/3/lzma/

def test():
    with lzma.open('small.xz', 'rb') as f:
        file_content = f.read()
        print (file_content)

