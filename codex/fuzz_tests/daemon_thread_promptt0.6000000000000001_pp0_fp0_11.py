import threading
# Test threading daemon
import time
# Test time

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
    
    def run(self):
        print(f"Starting {self.name}")
        print_time(self.name, self.delay, 5)
        print(f"Finished {self.name}")

def print_time(name, delay, counter):
    while counter:
        time.sleep(delay)
        print(f"{name}: {time.ctime(time.time())}")
        counter -= 1

if __name__ == "__main__":
    thread1 = MyThread('Thread 1', 1)
    thread2 = MyThread('Thread 2', 2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('Exiting main thread')
