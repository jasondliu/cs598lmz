import sys, threading
threading.Thread(target=lambda: sys.stdout.write('test')).start()

# 5. 什么时候使用多线程？
# 在IO密集型任务中使用多线程会比多进程快很多，但是在CPU密集型任务中，多进程反而比多线程快很多。
# 这是因为，在CPU密集型任务中，进程之间的切换会比线程切换更加频繁，这样消耗的CPU会更多，所以多进程的效率
