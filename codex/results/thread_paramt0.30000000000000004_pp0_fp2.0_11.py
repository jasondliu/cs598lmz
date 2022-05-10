import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(10))))).start()

# 使用多线程打印0-9，两个线程同时进行
import threading
def action(max):
    for i in range(max):
        print(i)
threading.Thread(target=action, args=(10,)).start()
threading.Thread(target=action, args=(10,)).start()

# 使用多线程打印0-9，两个线程交替进行
import threading
def action(max, name):
    for i in range(max):
        print(name, i)
        threading.Event().wait(1)
threading.Thread(target=action, args=(10, 'A')).start()
threading.Thread(target=action, args=(10, 'B')).start()

# 使
