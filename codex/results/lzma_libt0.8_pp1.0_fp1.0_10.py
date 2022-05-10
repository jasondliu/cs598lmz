import lzma
lzma.decompress( rb( 'images/0.xz' ) )

# 也可以用
# with open( 'images/0.xz', 'rb' ) as rf:
#     with lzma.open( rf ) as f:
#         f.read()
