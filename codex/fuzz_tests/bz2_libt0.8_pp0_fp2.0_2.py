import bz2
bz2_compressor = bz2.BZ2Compressor()
 
with open('somefile.txt', 'rb') as input:
    with open('compressed.bz2', 'wb') as output:
        while True:
            block = input.read(1024)
    if not block:
        break
    output.write(bz2_compressor.compress(block))
 
output.write(bz2_compressor.flush())

# 5.17. 同时作用于数据块和元素上的转换操作
import os
import sys
import time
if sys.platform.startswith('win'):
    def counter():
        return _counter()
else:
    def counter():
        return os.getpid()
 
def count_down(n):
    while n > 0:
        yield n
        n -= 1
 
def _counter():
    for pid in count_down(5):
        time.sleep(1)
       
