import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello, world\n')).start()

#1.3.4 单个分支线程
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello, world\n')).start()
sys.stdout.write('Hello, world\n')

#1.3.5 使用多线程提高性能
import sys, threading
def hello():
    sys.stdout.write('Hello, world\n')
threading.Thread(target=hello).start()

#1.3.6 创建线程
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello, world\n')).start()

#1.3.7 创建线程
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello, world\n')).start
