import bz2
# Test BZ2Decompressor

a = 1
 
bz2_comp = bz2.BZ2File("my_logs.bz2","w")
for i in range(a):
    a = str(i)
    bz2_comp.write("{0}".format(a)+"\n")
bz2_comp.close()

bz2_decomp = bz2.BZ2Decompressor()
with open("my_logs.bz2", "rb") as in_file:
    with open("out", "wb") as out_file:
        while True:
            s = in_file.read()
            if not s:
                break
            d = bz2_decomp.decompress(s)
            out_file.write(d)

# for i in range(a):
#     print(i)

import struct
# Test Struct

for i in range(a):
    a = str(i)
    with open("struct.out", "ab") as out_file:
        out_file.write(struct
