import sys, threading

def run():
    while True:
        print("thread 1")

def run2():
    while True:
        print("thread 2")

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run2)

t1.start()
t2.start()

t1.join()
t2.join()
