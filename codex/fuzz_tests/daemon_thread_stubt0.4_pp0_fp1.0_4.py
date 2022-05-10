import sys, threading

def run():
    for i in range(10):
        print("Thread 1")

def run2():
    for i in range(10):
        print("Thread 2")

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done")
