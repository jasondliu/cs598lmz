import bz2
# Test BZ2Decompressor

file = bz2.BZ2File('c:/Users/Stas/Downloads/enwiki-latest-pages-articles.xml.bz2')
decompressor = bz2.BZ2Decompressor()

with file as f:
    for line in f:
        print(decompressor.decompress(line))


# import bz2
# import io
# import os
#
# file = bz2.BZ2File('c:/Users/Stas/Downloads/enwiki-latest-pages-articles.xml.bz2')
#
# with file as f:
#     for line in f:
#         print(line)

# import bz2
# import io
# import os
#
# file = bz2.BZ2File('c:/Users/Stas/Downloads/enwiki-latest-pages-articles.xml.bz2')
#
# with file as f:
#     for line in f:
#         print(line)
