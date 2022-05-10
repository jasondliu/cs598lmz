import sys, threading

def run():
    while True:
        print("thread 1")
        time.sleep(1)

def run2():
    while True:
        print("thread 2")
        time.sleep(1)

thread1 = threading.Thread(target=run)
thread2 = threading.Thread(target=run2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
