import sys, threading

def run():
    for i in range(0, 1000):
        print(threading.current_thread().getName() + ": " + i)
        sleep(0.001)

def test():
    t1 = threading.Thread(None, run)
    t2 = threading.Thread(None, run)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

test()
