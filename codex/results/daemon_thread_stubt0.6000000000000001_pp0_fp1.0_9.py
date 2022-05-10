import sys, threading

def run():
    global x, item
    x = 0
    item = threading.Lock()

    for i in range(0, 1000000):
        item.acquire()
        x += 1
        item.release()

    print(x)

run()
