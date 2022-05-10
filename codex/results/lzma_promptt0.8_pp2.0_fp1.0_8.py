import lzma
# Test LZMADecompressor Objects
def tlzma():
    # d = lzma.LZMADecompressor()
    # with open("test.xz", "rb") as f:
    #     buffer = f.read(1024)
    #     print(len(buffer))
    #     print(d.eof)
    #     for i in range(4):
    #         res = d.decompress(buffer)
    #         print(len(res))
    #         print(d.eof)
    #     res = d.decompress(buffer)
    #     print(len(res))
    #     print(d.eof)

    d = lzma.LZMADecompressor()
    with open("test.xz", "rb") as f:
        print("Before:")
        print("d.eof:", d.eof)
        print("d.needs_input:", d.needs_input)
        print("d.needs_input:", d.needs_input)
        print("d.needs_input:", d
