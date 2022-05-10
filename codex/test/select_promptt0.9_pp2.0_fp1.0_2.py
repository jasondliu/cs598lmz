import select
# Test select.select
# case 1: simulate data ready to receive
print('read from stdin:')
po = select.poll()
po.register(sys.stdin)
while True:
    print(po.poll())
    input()
    print(po.poll())

# case 2: simulate data next to write
print('write to stdout:')
po = select.poll()
po.register(sys.stdout, select.POLLOUT)
while True:
    print(po.poll())
    print('END')
    print(po.poll())


# ======================================
# 三个进程, 如何通信
import time
from multiprocessing import Pipe


class Client(object):
    """
    模拟客户端
    """
