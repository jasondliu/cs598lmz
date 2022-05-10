import sys, threading

def run():
    print("This is the main thread")
    for i in range(10):
        print("Hello from the main thread")
        time.sleep(1)

def worker():
    print("This is the worker thread")
    for i in range(10):
        print("Hello from the worker thread")
        time.sleep(1)

t = threading.Thread(target=worker)
t.start()
run()
