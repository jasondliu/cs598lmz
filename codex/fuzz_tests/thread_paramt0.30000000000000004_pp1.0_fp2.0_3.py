import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# 主线程退出时，子线程会被强制退出
# 可以使用join()来等待子线程结束
t = threading.Thread(target=lambda: sys.stdout.write('Hello from thread 3\n'))
t.start()
t.join()

# 可以使用Thread类的构造函数来创建线程
# 如果使用这种方式，必须显式地调用start()来启动线程
# 并且必须
