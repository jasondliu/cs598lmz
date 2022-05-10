import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor(format=lzma.FORMAT_RAW, filters=[
    {
        "id": lzma.FILTER_ARM,
        "dict_size": 1024 * 64,
        "pb": 2,
        "lp": 0,
        "lc": 3,
    },
    {
        "id": lzma.FILTER_X86,
        "dict_size": 1024 * 128,
        "pb": 2,
        "lp": 0,
        "lc": 3,
    },
    {
        "id": lzma.FILTER_X86,
        "dict_size": 1024 * 1024,
        "pb": 2,
        "lp": 0,
        "lc": 3,
    },
    {
        "id": lzma.FILTER_IA64,
        "dict_size": 1024 * 128,
        "pb": 2,
        "lp": 0,
        "lc": 3,
    },
    {
        "id": lzma.FILTER_P
