import sys, threading
threading.Thread(target=lambda: sys.stdout.write('threading.Thread\n')).start()

class MyThread(threading.Thread):
    def run(self):
        sys.stdout.write('MyThread\n')

MyThread().start()

class MyThread(threading.Thread):
    def run(self):
        sys.stdout.write('MyThread\n')

for i in range(4):
    MyThread().start()

class MyThread(threading.Thread):
    def run(self):
        global n
        lock.acquire()
        temp = n
        n = temp + 1
        sys.stdout.write('n=%d\n' % n)
        lock.release()

n = 0
lock = threading.Lock()
for i in range(4):
    MyThread().start()

class MyThread(threading.Thread):
    def run(self):
        global n
        lock.acquire()
        temp = n
        n = temp + 1
        sys.stdout.write('n=%d\n'
