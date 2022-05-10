import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# 线程中的异常
def action(i):
    print(i ** 32)

threading.Thread(target=action, args=(2,)).start()
threading.Thread(target=lambda: action(2)).start()

# 线程返回值
class Power:
    def __init__(self, i):
        self.i = i
    def action(self):
        return self.i ** 32

threading.Thread(target=Power(2).action).start()

# 多线程的锁
count = 0

def adder(addlock):
    global count
    with addlock:
        count = count + 1

addlock = threading.Lock()
threads = []
for i in range(100):
    thread = threading.Thread(target
