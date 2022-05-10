import lzma
lzma.FORMAT_ALONE

# Open a compressed file
#with \
#    lzma.open('some_file_u.xz', 'rb') as bob, \
#    lzma.open('some_file_u.lzma', 'rb') as charlie, \
#    lzma.open('some_file_cn.xz', 'rt', encoding='utf8') as dan, \
#    lzma.open('some_file_cn.lzma', 'rt', encoding='utf8') as eddie, \
#    lzma.open('some_file_en.xz', 'rt', newline='\n') as felix, \
#    lzma.open('some_file_en.lzma', 'rt', newline='\n') as george:
#    # Process bob, charlie, dan, eddie, felix, and george.
#    pass

# Open a compressed file with a preset dictionary
#lzc = lzma.LZMACompressor(dict_size=16 *
