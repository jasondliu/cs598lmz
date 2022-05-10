import lzma
lzma.LZMAError().args

# Arguments invalid: []
lzma.LZMAOptions().args

# Arguments invalid: []
# Result type: None
# Result value: None
lzma.LZMAOptions().filter(x)

# Arguments type: (531,)
# Arguments value: (25,)
# Result type: int
# Result value: 1010
lzma.LZMAOptions().filter(x)._decode_lc()

# Arguments type: (531,)
# Arguments value: (25,)
# Result type: int
# Result value: 0
lzma.LZMAOptions().filter(x)._decode_lp()

# Arguments type: (531,)
# Arguments value: (25,)
# Result type: int
# Result value: 0
lzma.LZMAOptions().filter(x)._decode_pb()


# Arguments invalid: []
# Result type: None
# Result value: None
lzma.LZMAOptions()._encode_lc()

