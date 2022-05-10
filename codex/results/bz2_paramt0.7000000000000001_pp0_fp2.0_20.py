from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(inp)

# uncompress
# with open('file', 'rb') as f:
#     d = bz2.BZ2Decompressor()
#     file_content = d.decompress(f.read())

# print(file_content)


# def bz2_compress(data):
#     return bz2.compress(data.encode('utf-8'))
#
#
# def bz2_uncompress(data):
#     return bz2.decompress(data).decode('utf-8')
#
#
# if __name__ == '__main__':
#     s = 'hello world!hello world!hello world!hello world!'
#     print(bz2_uncompress(bz2_compress(s)))
#
#     # test
#     assert bz2_uncompress(bz2_compress(s)) == s
