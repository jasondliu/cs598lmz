import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()

def action(i):
    print(i ** 32)

class Power:
    def __init__(self, i):
        self.i = i
    def __call__(self):
        print(self.i ** 32)

t = threading.Thread(target=action, args=(2,))
u = threading.Thread(target=Power(2))
t.start()
u.start()

def action(max):
    for i in range(max):
        print(threading.currentThread().getName() + ' ' + str(i))
        time.sleep(1)

threads = []
for i in range(2):
    t = threading.Thread(target=action, args=(5,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

class Mythread(threading.
