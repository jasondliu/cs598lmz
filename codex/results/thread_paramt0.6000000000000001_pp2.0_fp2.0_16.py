import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()


# 方法3: 使用线程队列
import threading, queue

def stdin(q):
    while True:
        q.put(input())

q = queue.Queue()
t = threading.Thread(target=stdin, args=(q,))
t.daemon = True
t.start()

while True:
    print(q.get())


# 方法4: 使用键盘事件
import sys, threading, time

def keypress():
    while True:
        sys.stdout.write(sys.stdin.read(1))

t = threading.Thread(target=keypress)
t.daemon = True
t.start()

while True:
    sys.stdout.write('.')
    sys.stdout.flush()
    time.sleep(1)
