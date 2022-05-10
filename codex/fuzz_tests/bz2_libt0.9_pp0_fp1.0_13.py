import bz2
bz2_result = []
for i in range(0, 5):
    bz2_result.append(bz2.compress(datastr))
print(bz2_result)

#(7) LZ4
import lz4
lz4_result = []
for i in range(0, 5):
    lz4_result.append(lz4.compress(datastr))
print(lz4_result)

#(8)LZ4_HC
import lz4
lz4_result = []
for i in range(0, 5):
    lz4_result.append(lz4.compressHC(datastr))
print(lz4_result)
