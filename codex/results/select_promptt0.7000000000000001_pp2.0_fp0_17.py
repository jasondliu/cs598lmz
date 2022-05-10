import select
# Test select.select

import os, time

for i in range(2):
    pid = os.fork()
    if pid == 0:
        for i in range(1,10):
            time.sleep(1)
            print("子进程：%s" % os.getpid())
        exit(0)
    else:
        for i in range(1,10):
            time.sleep(1)
            print("父进程：%s" % os.getpid())
        exit(0)
