import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# 使用threading模块创建线程
import threading
def action(max):
    for i in range(max):
        print(threading.current_thread().name + " " + str(i))

threading.Thread(target=action, args=(100,), name="新线程").start()
for i in range(100):
    if i == 20:
        jt = threading.Thread(target=action, args=(100,), name="被join的线程")
        jt.start()
        jt.join()
    print(threading.current_thread().name + " " + str(i))

# 线程同步
# 在多线程环境下
