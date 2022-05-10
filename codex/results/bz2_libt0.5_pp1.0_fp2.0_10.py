import bz2
bz2.decompress(bz2.compress(b"Hello World"))

# json
import json
json.dumps([1,2,3,4,5,6])
json.loads('["foo", {"bar": ["baz", null, 1.0, 2]}]')

# 串行化
import pickle
pickle.dumps([1,2,3,4,5,6])
pickle.loads(b'\x80\x03]q\x00(K\x01K\x02K\x03K\x04K\x05K\x06e.')

# 内存映射文件
import mmap

# 分页和堆分配
import sys
sys.getsizeof(1)
sys.getsizeof([])
sys.getsizeof(())
sys.getsizeof({})
sys.getsizeof(set())

# 数学
import math
math.cos(math.pi/4)

