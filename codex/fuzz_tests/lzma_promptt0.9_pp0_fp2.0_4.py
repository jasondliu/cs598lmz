import lzma
# Test LZMADecompressor
c = lzma.LZMADecompressor()
bufsize = 4096
with open("/home/mseki/git/caget_plot/iocStats_8hr/iocStats_2017-07-25_20.iocStats") as input:
    with lzma.open(input) as f:
        with open("/home/mseki/git/caget_plot/iocStats_8hr/iocStats_2017-07-25_20_decompressed.iocStats", "wb") as output:
            while True:
                block = f.read(bufsize)
                if not block:
                    break
                output.write(c.decompress(block))

# Truncated file test
# with open("/home/mseki/git/caget_plot/iocStats_8hr/iocStats_2017-07-25_20.iocStats", "rb") as input:
#     with open("/home/mseki/git/caget_plot/iocStats_8hr/
