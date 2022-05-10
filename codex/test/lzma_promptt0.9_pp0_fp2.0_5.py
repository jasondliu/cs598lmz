import lzma
# Test LZMADecompressor.input() behavior
input_list = [b"123", b"456", b"789\n"]
input_prefixes = [b"i", b"m", b"p", b"o", b"r", b"t", b"a", b" ", b"s", b"n"
                  ]
eofs = [b"e", b"o", b"f", b"", b" ", b"", b" "]
decomp = lzma.LZMADecompressor()
for p in input_prefixes:
    for e in eofs:
        input = b"".join(input_list)
        while input:
            chunk = p + input[:3] + e
            #print("chunk:", chunk)
            input = input[3:]
