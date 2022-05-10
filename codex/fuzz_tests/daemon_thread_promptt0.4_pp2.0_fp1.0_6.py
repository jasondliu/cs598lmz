import threading
# Test threading daemon
import time

class MyThread(threading.Thread):
    def run(self):
        while True:
            print("Hello, world!")
            time.sleep(1)

if __name__ == "__main__":
    t = MyThread()
    t.setDaemon(True)
    t.start()
    time.sleep(5)
    print("main thread exits")
