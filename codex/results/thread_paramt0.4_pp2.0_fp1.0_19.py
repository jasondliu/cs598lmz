import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# 如果你想等待线程执行完毕，可以使用 threading.Thread.join() 方法。
# 以下例子会等待线程执行完毕，然后打印一条信息：
import time
def delayed():
    print('worker running')
t1 = threading.Thread(target=delayed)
t1.start()
t1.join()
print('program end')

# 如果你想让线程执行一段时间后再终止，可以使用 thread
