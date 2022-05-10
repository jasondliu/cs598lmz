import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from Python\n")).start()

# 启动一个进程
from multiprocessing import Process
Process(target=lambda: sys.stdout.write("Hello from a separate process\n")).start()

# 启动线程时，给线程命名
t = threading.Thread(target=lambda: sys.stdout.write("Hello from a named thread\n"))
t.name = "PythonThread"
t.start()

# 访问线程对象，获取线程名称
print(threading.current_thread().name)
print(threading.enumerate())

# 使用threading.Thread类的子类，把所有的逻辑放在构造器中，在run方
