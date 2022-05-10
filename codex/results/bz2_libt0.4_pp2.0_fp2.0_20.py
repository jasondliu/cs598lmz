import bz2
bz2.decompress(bz2.compress(data))

import gzip
gzip.decompress(gzip.compress(data))

import lzma
lzma.decompress(lzma.compress(data))

# 使用多进程压缩
import bz2
from multiprocessing import Pool

def run(data):
    return bz2.compress(data)

p = Pool(3)
p.map(run, [data, data, data])

# 使用多线程压缩
import bz2
from threading import Thread

class CompressThread(Thread):
    def __init__(self, data):
        super().__init__()
        self.data = data
    def run(self):
        return bz2.compress(self.data)

CompressThread(data).start()
CompressThread(data).start()
CompressThread(data).start()

# 压缩
