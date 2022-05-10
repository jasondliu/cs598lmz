import sys, threading

def run():
    while True:
        print(threading.currentThread().getName())
        sys.stdout.flush()
        time.sleep(1)

for _ in range(5):
    threading.Thread(target=run).start()

threading.Thread(target=run).start()

class MyThread(threading.Thread):
    def run(self):
        print(self.name)
        sys.stdout.flush()
        time.sleep(1)

for _ in range(5):
    MyThread().start()
