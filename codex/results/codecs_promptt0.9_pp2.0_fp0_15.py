import codecs
# Test codecs.register_error

def make_encoding_map(decoding_error):
    return { 128: unichr(0x041F)
             , 129: decoding_error
             , 130: unichr(0x0439)
             , 131: unichr(0x0446)
             , 132: unichr(0x0443)
             , 133: unichr(0x043A)
             , 134: unichr(0x0435)
             , 135: unichr(0x043D)
             , 136: unichr(0x0433)
             , 137: unichr(0x0448)
             , 138: unichr(0x0449)
             , 139: unichr(0x0437)
             , 140: unichr(0x0445)
             , 141: unichr(0x044A)
             , 142: unichr(0x005D)
             , 143: unichr(0x005B)
             , 144: unichr(0x0440)
             , 145: unich
