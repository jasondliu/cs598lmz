import bz2
bz2file = bz2.BZ2File("input.txt.bz2")
data = bz2file.read()
print(data)
bz2file.close()

#
# io_bz2.py
#
"""
结果与BZ2File一样，只是不需要关闭
"""
import bz2
with bz2.open("input.txt.bz2") as f:
    data = f.read()
    print(data)
