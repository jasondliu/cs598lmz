import threading
# Test threading daemon
# https://medium.com/@s8sachin/python-threads-vs-multiprocessing-vs-asyncio-c5b9a28a8b56
import random
import queue
import time

# 10,000,000
#     1 4.3954548
#     2 2.6232968
#     4 1.5647591
#     8 1.5590177
#    16 1.6512095
#    32 1.6466551
#    64 1.5724097
#   128 1.6718232
#   256 1.6412095
#   512 1.6412036
#  1024 1.6506230
#  2048 1.6372629
#  4096 1.6433029
#  8192 1.6295644
# 16384 1.6430378
# 32768 1.6479579
# 65536 1.6463521
#131072 1.6444702

def worker(l):
    while True:
        item = l.get()
        if item is None
