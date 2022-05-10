import lzma
# Test LZMADecompressor
# https://pymotw.com/3/lzma/

def test():
    with lzma.open('small.xz', 'rb') as f:
        file_content = f.read()
        print (file_content)

test()

def test2():
    with lzma.open('small.xz', 'rb') as f:
        decompressor = lzma.LZMADecompressor()
        file_content = decompressor.decompress(f.read())
        print (file_content)

test2()

def test3():
    with lzma.open('small.xz', 'rb') as f:
        decompressor = lzma.LZMADecompressor()
        file_content = decompressor.decompress(f.read())
        print (file_content)

test3()

def test4():
    with lzma.open('small.xz', 'rb') as f:
        decompressor = lzma.LZMADecompressor()
        file
