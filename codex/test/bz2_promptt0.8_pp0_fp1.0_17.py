import bz2
# Test BZ2Decompressor

a = 1
 
bz2_comp = bz2.BZ2File("my_logs.bz2","w")
for i in range(a):
    a = str(i)
