import bz2
bz2_compressor = bz2.BZ2Compressor()
with bz2.open('compressed.bz2', 'wb') as f:
   for data in ['line 1', 'line 2', 'line 3', 'line 4'] :
       f.write(bz2_compressor.compress(data))
   f.write(bz2_compressor.flush())

# with bz2.open('compressed.bz2', 'rb') as f:
#     content = f.read()
#     print(content)
#
#
# ##############################################################################
#
import bz2
bz2_compressor = bz2.BZ2Compressor()
with bz2.open('compressed.bz2', 'wb') as f:
    for data in ['line 1', 'line 2', 'line 3', 'line 4']:
        f.write(bz2_compressor.compress(data))
    f.write(bz2_compressor.flush())

with bz2.open('compressed.b
